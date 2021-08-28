import requests
from bs4 import BeautifulSoup

url1 = "https://www.trendyol.com/apple/macbook-air-13-m1-8gb-256gb-ssd-uzay-grisi-mgn63tu-a-p-68042136?boutiqueId=579136&merchantId=436484"

headers = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36" 
}

page = requests.get(url1, headers=headers)

htmlPage = BeautifulSoup(page.content,'html.parser')

productTitle = htmlPage.find("h1", class_="pr-new-br").getText()

price = htmlPage.find("span",class_="prc-slg").getText()

convertedPrice = float(price.replace(",",".").replace(" TL",""))

if(convertedPrice <= 150):
    print("Ürün fiyatı düştü")

print(convertedPrice)