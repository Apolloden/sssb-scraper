from bs4 import BeautifulSoup
import requests

url = "https://sssb.se/soka-bostad/sok-ledigt/lediga-bostader/?pagination=0&paginationantal=0"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# get number of available apartments on SSSB
availabilty = doc.find("h2")
parent = availabilty.parent
theAvailable = parent.find(class_="f2-widget Loading Objektsummering Lagenheter") # gives 0 for some reason

# get a table of available apartments
table = doc.find(class_="f2-widget  Objektlistabilder Lagenheter")

address = doc.find_all("ObjektAdress")

print(table)
print(address)