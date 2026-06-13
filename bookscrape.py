import requests 

from bs4 import BeautifulSoup

import pandas as pd 

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
        "price": price.replace("£", "") # remove the pound sign from the price. method chaining is when we call multiple methods on the same object. In this case, we are calling the replace method on the price string.
    }
    all_scraped_books.append(book_item)

#print(all_scraped_books)

# pandas is a library that allows us to create a dataframe, which is a table that can hold our data in a structured way

df = pd.DataFrame(all_scraped_books)    # pd will 

#df.to_csv("scraped_books.csv", index=False) # index=False means we don't want to include the index column in the csv file

df.to_excel("scraped_books.xlsx", index=False) # we can also save the dataframe as an excel file. we need to install the openpyxl library to do this. pip install openpyxl