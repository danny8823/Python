from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4095833510&distance=25&geoId=103940382&keywords=javascript%20developer&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")

# sign_in_button = driver.find_element(
#     by=By.CLASS_NAME, value='nav__button-secondary')

# sign_in_button.click()

# username_input = driver.find_element(by=By.ID, value="username")
# password_input = driver.find_element(by=By.ID, value="password")

# username_input.send_keys("dannyyoo714@gmail.com")
# password_input.send_keys("Yoitsdannyoo8!")

# login_form_signin_button = driver.find_element(
#     by=By.CLASS_NAME, value='btn__primary--large')

# login_form_signin_button.click()

# jobs_link = driver.find_element(
#     by=By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')

# jobs_link.click()

# jobs_search_input = driver.find_element(
#     by=By.ID, value='jobs-search-box-keyword-id-ember539')

# jobs_search_input.click()
# jobs_search_input.send_keys('web developer')
