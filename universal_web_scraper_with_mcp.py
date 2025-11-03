import os
import re
import requests
import mimetypes
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from docx import Document
import time

visited = set()

def url_to_filename(url, ext='txt'):
    url = re.sub(r'https?://', '', url)
    url = url.replace('/', '__')
    return quote(url, safe='') + f'.{ext}'

def save_txt(output_dir, filename, content):
    path = os.path.join(output_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def save_docx(output_dir, filename, content):
    path = os.path.join(output_dir, filename)
    doc = Document()
    doc.add_paragraph(content)
    doc.save(path)

def scrape_js_page(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # You may need to specify the path to chromedriver if not globally installed
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)  # Wait for JS to load
    html = driver.page_source
    driver.quit()
    return html

def mock_mcp_analyze(text):
    # This is a placeholder for a real MCP tool integration!
    # Replace with real MCP API calls or SDK as needed.
    # Example: requests.post("https://api.mcp.com/analyze", json={"text": text})
    # For demonstration, return basic NLP analysis:
    word_count = len(text.split())
    summary = text[:200] + ("..." if len(text) > 200 else "")
    entities = re.findall(r'\b[A-Z][a-z]+\b', text)
    return {
        "summary": summary,
        "word_count": word_count,
        "entities": list(set(entities))[:10],  # Top 10 entities
        "classification": "Generic Webpage"
    }

def process_with_mcp(data):
    # Integrate with actual MCP tool here
    # You can process HTML, raw text, or any asset
    mcp_result = mock_mcp_analyze(data["text"])
    return mcp_result

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
        "images": [img.get('src') for img in soup.find_all('img')],
        "links": []
    }

    for a_tag in soup.find_all('a', href=True):
        link = urljoin(url, a_tag['href'])
        if is_internal_link(link, base_domain):
            data["links"].append(link)

    # MCP-powered processing
    mcp_result = process_with_mcp(data)

    # Save output as TXT or DOCX
    filename = url_to_filename(url, ext=filetype)
    save_func = save_docx if filetype == "docx" else save_txt
    save_func(
        output_dir,
        filename,
        f"URL: {url}\nTitle: {data['title']}\n\nText:\n{data['text']}\n\nImages:\n{data['images']}\n\nMCP Analysis:\n{mcp_result}"
    )

    # Recursively scrape internal links
    for link in data["links"]:
        if link not in visited:
            scrape_page(link, base_domain, output_dir, use_js, filetype)
            time.sleep(1)  # Be polite

def is_internal_link(link, base_domain):
    parsed_link = urlparse(link)
    return (parsed_link.netloc == '' or parsed_link.netloc == base_domain)

def main(start_url, use_js=True, filetype="txt"):
    visited.clear()  # Reset visited set for each new domain
    base_domain = urlparse(start_url).netloc
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, f"scraped_{base_domain}")
    os.makedirs(output_dir, exist_ok=True)
    scrape_page(start_url, base_domain, output_dir, use_js=use_js, filetype=filetype)

if __name__ == "__main__":
    # USAGE: Change start_url to the site you want to scrape
    # Scrape example.com
    main("https://example.com", use_js=True, filetype="txt")
    # Scrape anotherdomain.org
    # main("https://anotherdomain.org", use_js=True, filetype="txt")