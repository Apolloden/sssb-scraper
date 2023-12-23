from bs4 import BeautifulSoup
import requests

url = 'https://sssb.se/soka-bostad/sok-ledigt/lediga-bostader/?pagination=0&paginationantal=0'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

adress = soup.find_all('ObjektAdress')

tag = soup.title

# objects = soup.find('//*[@id="SubNavigationContentContainer"]/div[3]/div[4]')

# //*[@id="SubNavigationContentContainer"]/div[3]/div[4]

if __name__ == "__main__":
    # print(soup)
    # print(soup.prettify())
    print(tag)