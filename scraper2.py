from bs4 import BeautifulSoup
import requests

url = "https://sssb.se/widgets/?callback=jQuery17203404817715808992_1703443444188&widgets%5B%5D=alert&widgets%5B%5D=objektsummering%40lagenheter&widgets%5B%5D=objektfilter%40lagenheter&widgets%5B%5D=objektsortering%40lagenheter&widgets%5B%5D=objektlistabilder%40lagenheter&widgets%5B%5D=pagineringantal%40lagenheter&widgets%5B%5D=paginering%40lagenheter&widgets%5B%5D=pagineringgofirst%40lagenheter&widgets%5B%5D=pagineringgonew%40lagenheter&widgets%5B%5D=pagineringlista%40lagenheter&widgets%5B%5D=pagineringgoold%40lagenheter&widgets%5B%5D=pagineringgolast%40lagenheter"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# get number of available apartments on SSSB
availabilty = doc.find("strong")
availabiltyParent = availabilty.parent

# get a table of available apartments
#table = doc.find(class_="f2-widget  Objektlistabilder Lagenheter")

#address = doc.find_all("ObjektAdress")

# print(doc.prettify())

apartment = doc.find(class_ = "")
apartmentsinfo = doc.find_all("h4")
# print(apartment)

# Find the div tag with class 'Box' and objektlistitem attribute
target_div = doc.find('div', {'class': 'Box', 'objektlistitem': True})

# If the target div is found, you can extract its content
if target_div:
    content_below = target_div.find_all_next(text=True, strip=True)
    print("Content below target div:")
    for content in content_below:
        print(content)
else:
    print("Target div not found.")