from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(
    'https://www.python.org/')

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cent = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

# print(f"{price_dollar.text}.{price_cent.text}")

search_bar = driver.find_element(By.NAME, value="q")

button = driver.find_element(By.ID, value='submit')

doc_link = driver.find_element(
    By.CSS_SELECTOR, value='.documentation-widget a')


bug_link = driver.find_element(
    By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

driver.quit()
