import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tldextract

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.to_visit_urls = set([base_url])
        self.subdomains = set()

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_domain(self, url):
        ext = tldextract.extract(url)
        return f"{ext.domain}.{ext.suffix}"

    def get_subdomain(self, url):
        ext = tldextract.extract(url)
        return f"{ext.subdomain}.{ext.domain}.{ext.suffix}"

    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(base_url, href)
            if self.is_valid_url(full_url):
                links.add(full_url)
        return links

    def crawl(self):
        while self.to_visit_urls:
            current_url = self.to_visit_urls.pop()
            if current_url in self.visited_urls:
                continue

            print(f"Crawling: {current_url}")
            self.visited_urls.add(current_url)

            page_content = self.fetch_page(current_url)
            if page_content is None:
                continue

            domain = self.get_domain(self.base_url)
            subdomain = self.get_subdomain(current_url)

            if domain in subdomain:
                self.subdomains.add(subdomain)
                new_links = self.extract_links(page_content, current_url)
                self.to_visit_urls.update(new_links)

        print("\nCrawling complete. Visited URLs:")
        for url in self.visited_urls:
            print(url)

        print("\nDiscovered subdomains:")
        for subdomain in self.subdomains:
            print(subdomain)

if __name__ == "__main__":
    base_url = input("Enter the base URL to start crawling: ").strip()
    crawler = WebCrawler(base_url)
    crawler.crawl()
