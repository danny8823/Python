from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

property_address_link = []
property_address_string = []
property_address_price = []

with open('/Users/danny714/Desktop/Python/Day 53/zillow_html.txt', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

    property_address_html = soup.find_all(
        'a', class_='StyledPropertyCardDataArea-anchor')

    for address_link in property_address_html:
        property_address_link.append(address_link.get('href'))

    addresses = soup.find_all(
        'address', {'data-test': 'property-card-addr'})

    for address in addresses:
        property_address_string.append(address.text.strip())

    prices = soup.find_all('span', {'data-test': 'property-card-price'})

    for price in prices:
        property_address_price.append(price.text.strip())


print(len(property_address_link))
print(len(property_address_string))
print(len(property_address_price))


class ZillowForm:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_form(self):
        self.driver.get(
            "https://forms.gle/JaxL3e17sUoP4qWZ7")
        time.sleep(3)
        inputs = self.driver.find_elements(
            By.CLASS_NAME, value='whsOnd')

        inputs[0].send_keys(property_address_string[0])
        inputs[1].send_keys(property_address_price[0])
        inputs[2].send_keys(property_address_link[0])


bot = ZillowForm()
bot.get_form()
