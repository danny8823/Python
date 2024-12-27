from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

# article_number = driver.find_element(
#     "xpath", "//*[@title='Special:Statistics']")
article_number = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_number.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search_bar = driver.find_element(
    By.CLASS_NAME, value='cdx-text-input__input')

search_bar.send_keys('TESTING', Keys.ENTER)

# driver.quit()
