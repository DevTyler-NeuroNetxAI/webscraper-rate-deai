import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

visited = set()

def is_internal_link(link, base_domain):
    parsed_link = urlparse(link)
    return (parsed_link.netloc == '' or parsed_link.netloc == base_domain)

def scrape_page(url, base_domain):
    if url in visited:
        return
    print(f"Scraping: {url}")
    visited.add(url)
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Extract all info: text, images, links, etc.
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

    # Print or save data as required (here we just print the title)
    print(f"Title: {data['title']}")
    print(f"Images: {data['images']}")
    print(f"Text snippet: {data['text'][:200]}...")  # Print first 200 chars

    # Recursively scrape internal links
    for link in data["links"]:
        if link not in visited:
            scrape_page(link, base_domain)
            time.sleep(1)  # Be polite! Avoid hammering the server.

if __name__ == "__main__":
    start_url = "https://example.com"
    base_domain = urlparse(start_url).netloc
    scrape_page(start_url, base_domain)