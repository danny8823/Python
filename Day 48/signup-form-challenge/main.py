from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name_input = driver.find_element(By.NAME, value='fName')
last_name_input = driver.find_element(By.NAME, value='lName')
email_input = driver.find_element(By.NAME, value='email')
sign_up_button = driver.find_element(By.TAG_NAME, 'button')
# sign_up_button = driver.find_element(By.CSS_SELECTOR, value = 'form button')
first_name_input.send_keys('Danny')
last_name_input.send_keys('Yoo')
email_input.send_keys('dannyyoo714@gmail.com')
sign_up_button.click()
