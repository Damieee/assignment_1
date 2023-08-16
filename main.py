import requests
from bs4 import BeautifulSoup

def scrape_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        links = []

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)

        return links

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def write_to_txt(links):
    with open("links.txt", "a") as f:
        for link in links:
            f.write(f"{link}\n")

if __name__ == "__main__":
    website_url = "https://www.foxbusiness.com/technology/amazon-launches-ai-generated-product-review-summaries"
    scraped_links = scrape_links(website_url)
    write_to_txt(scraped_links)
    
