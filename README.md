# PDF Link Scraper

This project is a simple web scraper that extracts PDF links from a specified web page and checks their availability. The available links are then saved to a file named `links.py`.

## Requirements

- Python 3.11 or higher
- `beautifulsoup4` library
- `requests` library

## Installation

Install the required dependencies using pip:

```py
pip install beautifulsoup4 requests
```

## Usage

1. Update the URL in the `main` function of `scraper.py` to the web page you want to scrape.
2. Run the scraper:

```py
python scraper.py
```

1. The available PDF links will be printed to the console and saved to `links.py`.

## Files

- `scraper.py`: The main script that performs the web scraping and link checking.
- `links.py`: The file where available PDF links are saved.
