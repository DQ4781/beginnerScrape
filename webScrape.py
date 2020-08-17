import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+cards"
# opening up the connection, grabbing the page
uClient = uReq(url)
# We save it to a variable bc if we call the read() func, we 'dump' the webpage and it gets lost
page_html = uClient.read()
# closing the client
uClient.close()
# parse the text from uClient into a html file
page_soup = soup(page_html, "html.parser")
# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)


for container in containers:
    brand = container.div.div.a.img["title"]
    name = container.a.img["title"]
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text

    print(brand)
    print(name)
    print(shipping)

    f.write(brand + "," + name.replace(",", "|") + "," + shipping + "\n")

f.close()
