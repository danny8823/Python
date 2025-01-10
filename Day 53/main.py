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


class ZillowForm:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_form(self):
        self.driver.get(
            "https://forms.gle/JaxL3e17sUoP4qWZ7")
        time.sleep(3)

        for num in range(len(property_address_link)):
            inputs = self.driver.find_elements(
                By.CLASS_NAME, value='whsOnd')
            address_input = inputs[0]
            price_input = inputs[1]
            link_input = inputs[2]

            if num == range(len(property_address_link)):
                print('done')

            time.sleep(2)
            address_input.send_keys(property_address_string[num])
            price_input.send_keys(property_address_price[num])
            link_input.send_keys(property_address_link[num])

            time.sleep(2)

            submit = self.driver.find_element(
                By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')

            submit.click()

            time.sleep(2)

            submit_another_response = self.driver.find_element(
                By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')

            submit_another_response.click()


bot = ZillowForm()
bot.get_form()
