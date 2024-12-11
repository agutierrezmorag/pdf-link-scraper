import urllib.parse

import requests
from bs4 import BeautifulSoup


def check_url_availability(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False


def main():
    # URL of the web page to scrape
    url = "https://www.unap.cl/prontus_unap/site/artic/20171006/pags/20171006150628.html"  # Replace with the actual URL

    # Send a GET request to the web page
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links on the page
    links = soup.find_all("a")

    base_url = "https://www.unap.cl/"

    # Filter links that end with .pdf and add base URL if necessary
    pdf_links = [
        link.get("href")
        if link.get("href").startswith("http")
        else base_url + link.get("href")
        for link in links
        if link.get("href") and link.get("href").endswith(".pdf")
    ]

    available_pdf_links = []

    # Print all available PDF links
    for pdf_link in pdf_links:
        if check_url_availability(pdf_link):
            print(f"Available: {pdf_link}")
            available_pdf_links.append(pdf_link)
        else:
            print(f"Unavailable: {pdf_link}")

    # Save available links to links.py
    with open("links.py", "w") as file:
        file.write("available_links = [\n")
        for link in available_pdf_links:
            encoded_link = urllib.parse.quote(link, safe=":/")
            file.write(f"    '{encoded_link}',\n")
        file.write("]\n")


if __name__ == "__main__":
    main()
