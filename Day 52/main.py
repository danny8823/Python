from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTA_ACCT = 'dannydoyoo714@gmail.com'
INSTA_PASS = 'Danny8823!'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        email_input = self.driver.find_element(
            By.CSS_SELECTOR, value='input[aria-label="Phone number, username, or email"]')
        email_input.send_keys(INSTA_ACCT)

        pass_input = self.driver.find_element(
            By.CSS_SELECTOR, value='input[aria-label="Password"]'
        )
        pass_input.send_keys(INSTA_PASS)

        login_button = self.driver.find_element(
            By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button'
        )

        login_button.click()

        time.sleep(9)

        not_now_button = self.driver.find_element(
            By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div'
        )

        not_now_button.click()

    def find_followers(self):
        self.driver.get(
            'https://www.instagram.com/that.plumber.dude/followers')
        time.sleep(5)
        followers_list = self.driver.find_element(
            By.XPATH, value='//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers_list.click()
        time.sleep(3)
        dialog = self.driver.find_element(
            By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(2)

    def follow(self):
        print('start')
        dialog = self.driver.find_element(
            By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        all_buttons = dialog.find_elements(By.TAG_NAME, value='button')
        for button in all_buttons:
            print('hello')
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(
                    by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()


bot.find_followers()
bot.follow()
