import requests 

from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"

response = requests.get(url)

print(response.status_code)

# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

cards = soup.select(".product_pod")

#print(cards)

print(cards[0]) #selecting the first book

# create a variable to hold the title and price of the first book
all_scraped_books = []

for card in cards:
    title = card.select_one("h3 a").text
    price = card.select_one(".price_color").text # for a class, we use a dot before the class name

    #print(f"{title} - {price}")

    # create a dictionary to hold the title and price of each book
    book_item = {
        "title": title,
        "price": price
    }
    all_scraped_books.append(book_item)

print(all_scraped_books)




