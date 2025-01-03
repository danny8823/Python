from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_UP = 10
X_EMAIL = 'dannyyoo714@gmail.com'
X_PASSWORD = 'Hello_there714!'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.speedtest.net/')

print('start')
get_speed_button = driver.find_element(by=By.CLASS_NAME, value='js-start-test')
get_speed_button.click()
print('sleep start')
time.sleep(200)
pop_up = driver.find_element(
    by=By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
pop_up.click()
print('sleep over')
get_speed_int = driver.find_element(
    by=By.CLASS_NAME, value='download-speed')
print(get_speed_int.text)
# def get_speed_int():
#     print('start')
#     get_speed_button = driver.find_element(
#         by=By.CLASS_NAME, value='js-start-test')
#     time.sleep(120)
#     print('sleep over')
#     get_speed_button.click()
#     time.sleep(240)
#     get_speed_int = driver.find_element(
#         by=By.CLASS_NAME, value='result-data-large number result-data-value download-speed')
#     print(get_speed_int)


# get_speed_int()
