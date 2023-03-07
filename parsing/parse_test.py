import json
import requests
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://us.puma.com/us/en'

# def get_soup(url:str) -> BS:
response = requests.get(BASE_URL)
print(response)
    # soup = BS(response.text, 'lxml')
    # return soup
