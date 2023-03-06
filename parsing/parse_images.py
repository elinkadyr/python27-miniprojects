import requests, json

image_url = 'https://www.kivano.kg/images/product/111895/1665049627_16517300.jpg'

response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)