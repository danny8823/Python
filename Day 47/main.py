from bs4 import BeautifulSoup
import requests
practice_url = 'https://appbrewery.github.io/instant_pot/'
live_url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
response = requests.get(url=live_url)

soup = BeautifulSoup(response.text, 'html.parser')
price_dollar = soup.find(class_='a-price-whole').get_text()
price_cent = soup.find(class_='a-price-fraction').get_text()
print(price_dollar + price_cent)
