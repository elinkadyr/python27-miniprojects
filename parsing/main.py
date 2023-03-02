import requests
from bs4 import BeautifulSoup

main_url = 'https://www.kivano.kg/'

response = requests.get(main_url)  #отправляем запрос
# print(response.text)  #html-str


soup = BeautifulSoup(response.text, 'lxml')

phones_span = soup.find('span', {"id":"phones"})
raw_phones = phones_span.text
phones_list = []

for ph in raw_phones.split("\n"):
    clear_phone = ph.replace('\r', '').strip()
    if clear_phone:
        phones_list.append(clear_phone)

# print(phones_list)

"Детализация продукта"

product_url = 'product/view/smart-chasy-apple-watch-ultra-49mm-alpine-loop-oranzhevye'

response = requests.get(main_url+product_url)
soup = BeautifulSoup(response.text, 'lxml')
product_card = soup.find('div', {"class":"product-view oh"})
# print(product_card)
title = product_card.find('h1').text
# print(title)

# print(len(product_card.find_all('img')))

image_box = product_card.find('div', {'class':'img_full addlight'})
image = image_box.find('img').get('src')
# print(image)
# print(image_box.find_all('img'))

price = product_card.find('span', {'itemprop':'price'}).text
# print(price)

data = {'title':title, 'image':image, 'price':price}

print(data)