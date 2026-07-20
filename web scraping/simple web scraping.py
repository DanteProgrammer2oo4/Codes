import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)   # get a website

soup = BeautifulSoup(   # html Analysis
    response.text,
    "html.parser"
)


book = soup.find(
    "article",
    class_ = "product_pod"
)
title = book.h3.a["title"] # get (h3) a book name
print(title)

#--------------------------------------------------

books = soup.find_all( # get all books name & price
    "article",
    class_ = "product_pod"
)

for book in books:
    title = book.h3.a["title"]
    price = book.find(
        "p",
        class_ = "price_color"
    ).text
    rate = book.find(
        "p",
        class_="star-rating"
    )

    rating = rate["class"][1]
    
    print(title)
    print(f'price : {price}')
    print(f'rating : {rating}')
    (print("-" * 30))

