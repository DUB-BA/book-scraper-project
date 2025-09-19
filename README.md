# Static E-Commerce Book Scraper

This project is a complete and robust Python script designed to scrape all 1,000 book listings from the static e-commerce sandbox `books.toscrape.com`.

## Core Technologies
- **Python 3**
- **Requests:** For efficient and reliable fetching of HTML content from the server.
- **BeautifulSoup4:** For parsing complex and messy HTML to accurately extract target data.
- **Python CSV Module:** For writing the scraped data into a structured, universally-usable format.

## Key Features & Challenges Solved
- **Multi-Page Crawling:** The script automatically discovers and follows the "Next" page link, enabling it to crawl through all 50 pages of the catalogue without manual intervention.
- **Intelligent Data Cleaning:** The script performs on-the-fly data transformation:
  - **Prices:** Converts price strings like "£51.77" into numerical floats (`51.77`) for analysis.
  - **Star Ratings:** Intelligently parses the star rating (e.g., "Three") from the element's class name and converts it into an integer (`3`).
- **Structured Export:** The final output is a clean `books_data.csv` file, ready for import into any database or spreadsheet software.
