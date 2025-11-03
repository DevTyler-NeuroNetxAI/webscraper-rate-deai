import os
import re
import requests
import mimetypes
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from docx import Document as DocxDocument
import PyPDF2
import pandas as pd
import time

visited = set()
downloaded_files = set()

def url_to_filename(url, ext='txt'):
    url = re.sub(r'https?://', '', url)
    url = url.replace('/', '__')
    return quote(url, safe='') + f'.{ext}'

def save_txt(output_dir, filename, content):
    path = os.path.join(output_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_docx(path):
    doc = DocxDocument(path)
    return '\n'.join([p.text for p in doc.paragraphs])

def extract_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_csv(path):
    df = pd.read_csv(path)
    return df.to_string()

def extract_xlsx(path):
    df = pd.read_excel(path)
    return df.to_string()

def mock_mcp_analyze(text):
    word_count = len(text.split())
    summary = text[:200] + ("..." if len(text) > 200 else "")
    entities = re.findall(r'\b[A-Z][a-z]+\b', text)
    return {
        "summary": summary,
        "word_count": word_count,
        "entities": list(set(entities))[:10],
        "classification": "Document"
    }

def process_with_mcp(data):
    mcp_result = mock_mcp_analyze(data["text"])
    return mcp_result

def download_and_extract_doc(asset_url, output_dir):
    try:
        resp = requests.get(asset_url, timeout=30)
        resp.raise_for_status()
        ext = asset_url.split('.')[-1].lower()
        filename = url_to_filename(asset_url, ext)
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(resp.content)
        downloaded_files.add(asset_url)
        # Extract content
        if ext == "docx":
            text = extract_docx(file_path)
        elif ext == "pdf":
            text = extract_pdf(file_path)
        elif ext == "csv":
            text = extract_csv(file_path)
        elif ext in ["xlsx", "xls"]:
            text = extract_xlsx(file_path)
        else:
            text = None
        # Process with MCP if possible
        if text:
            mcp_result = process_with_mcp({"text": text})
            save_txt(output_dir, filename + ".txt", f"Extracted from {asset_url}\n\nText:\n{text}\n\nMCP Analysis:\n{mcp_result}")
    except Exception as e:
        print(f"Failed to download/extract {asset_url}: {e}")

def scrape_js_page(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    driver.quit()
    return html

def scrape_page(url, base_domain, output_dir, use_js=False, filetype="txt"):
    if url in visited:
        return
    print(f"Scraping: {url}")
    visited.add(url)
    try:
        html = ''
        if use_js:
            html = scrape_js_page(url)
        else:
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            html = resp.text
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return

    soup = BeautifulSoup(html, 'html.parser')
    data = {
        "url": url,
        "title": soup.title.string if soup.title else "",
        "text": soup.get_text(),
        "links": [],
        "documents": []
    }

    for a_tag in soup.find_all('a', href=True):
        link = urljoin(url, a_tag['href'])
        if is_internal_link(link, base_domain):
            data["links"].append(link)
        elif is_document_link(link) and link not in downloaded_files:
            data["documents"].append(link)
            download_and_extract_doc(link, output_dir)

    # MCP-powered processing
    mcp_result = process_with_mcp(data)

    filename = url_to_filename(url, ext=filetype)
    save_func = save_txt  # For simplicity, txt output
    save_func(
        output_dir,
        filename,
        f"URL: {url}\nTitle: {data['title']}\n\nText:\n{data['text']}\n\nDocuments:\n{data['documents']}\n\nMCP Analysis:\n{mcp_result}"
    )

    for link in data["links"]:
        if link not in visited:
            scrape_page(link, base_domain, output_dir, use_js, filetype)
            time.sleep(1)

def is_internal_link(link, base_domain):
    parsed_link = urlparse(link)
    return (parsed_link.netloc == '' or parsed_link.netloc == base_domain)

def is_document_link(link):
    doc_types = ["docx", "pdf", "csv", "xlsx", "xls", "pptx", "txt"]
    return any(link.lower().endswith(f".{ext}") for ext in doc_types)

def main(start_url, use_js=True, filetype="txt"):
    visited.clear()
    downloaded_files.clear()
    base_domain = urlparse(start_url).netloc
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, f"scraped_{base_domain}")
    os.makedirs(output_dir, exist_ok=True)
    scrape_page(start_url, base_domain, output_dir, use_js=use_js, filetype=filetype)

if __name__ == "__main__":
    main("https://example.com", use_js=True, filetype="txt")