import requests
from bs4 import BeautifulSoup
import csv

with open("books_data.csv", "w", newline="", encoding="utf-8") as csv_file:

    writer = csv.writer(csv_file)
    writer.writerow(["Title, Price, Rating"])

    base_url = "https://books.toscrape.com/"
    current_url = base_url

    while current_url:
        try:
            response = requests.get(current_url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Could not retrieve page: {e}")
        else:
            soup = BeautifulSoup(response.text, "lxml")

            books = soup.select("article.product_pod")
            ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").get_text().strip("Â")
                stars = book.find("p", class_="star-rating")["class"][1]

                print(title)
                print(price)
                print(ratings[stars])
                writer.writerow([title, price, ratings[stars]])

            next_page_button = soup.find("li", class_="next")
            if next_page_button:
                link_page = next_page_button.a["href"]
                new_page = base_url + link_page
                if "catalogue/" not in new_page:

                    fixed_url = base_url + "catalogue/" + link_page
                    current_url = fixed_url
                    print(f"Going to {current_url}...")
                else:
                    current_url = new_page
                    print(f"Going to {current_url}...")
            else:
                print("No more pages found")
                break
