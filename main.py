import requests
from bs4 import BeautifulSoup

def scrape_headline_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        headline_links = []

        for headline in soup.find_all(['h1', 'h2', 'h3'], class_='title'):
            link = headline.find('a')
            if link:
                href = link.get('href')
                if href:
                    headline_links.append(href)

        return headline_links

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def write_to_txt(links):
    with open("links.txt", "a") as f:
        for link in links:
            f.write(f"{link}\n")

if __name__ == "__main__":
    website_url = "https://www.foxbusiness.com"
    scraped_headline_links = scrape_headline_links(website_url)
    write_to_txt(scraped_headline_links)
