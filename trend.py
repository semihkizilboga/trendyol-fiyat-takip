import requests
from bs4 import BeautifulSoup
from send import sendMail

url = "https://www.trendyol.com/apple/macbook-air-13-m1-8gb-256gb-ssd-uzay-grisi-mgn63tu-a-p-68042136?boutiqueId=579136&merchantId=436484"

headers = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36" 
}

page = requests.get(url1, headers=headers)

htmlPage = BeautifulSoup(page.content,'html.parser')

productTitle = htmlPage.find("h1", class_="pr-new-br").getText()

price = htmlPage.find("span",class_="prc-slg").getText()

image = htmlPage.find("img",class_="ph-gl-img")

convertedPrice = float(price.replace(",",".").replace(" TL",""))

if(convertedPrice <= 550):
    print("Ürün fiyatı düştü")
    htmlEmailContent = """
        <html>
        <head></head>
        <body>
        <div style="display:flex; justify-content:center; background: linear-gradient(90deg, rgba(168,21,66,1) 0%, rgba(59,0,255,1) 100%); width:80rem; padding:5px; border-radius:10px;">
        {2}<br/>
        <div style="padding-left:20px;">
        <h3 style="color:white; font-size:30px;">{1}</h3>

        <div>
        <p style="color:white; font-size:25px;">Güncel Fiyat: {0}</p>
        </div>
        
        <div>
        <p style="color:white; font-size:20px;">Ürün Linki: <a style="color:blue;" href="{3}">Tıkla</a></p>
        </div>
        </div>
        </div>
        
        </body>
        </html>
        """.format(price, productTitle, image, url)
    sendMail("paradoxcoming@gmail.com","Ürünün fiyatı düştü",htmlEmailContent)

print(convertedPrice)
