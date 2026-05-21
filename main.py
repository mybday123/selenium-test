from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Feature: User logs in
#   Scenario: User logs in with valid username and password
#       Given the user has an existing account
#       And the user in on the login page
#       When the user enters a valid username and password
#       Then the user is redirected to a secure page
#       And show login successful banner
#
#   Scenario: User logs in with valid username but invalid password
#       Given the user has an existing account
#       And the user is on the login page
#       When the user enters a valid username but invalid password
#       Then website will reject the login
#       And show an invalid password error banner to the user

LOGIN_URL = "https://the-internet.herokuapp.com/login"
SECURE_URL = "https://the-internet.herokuapp.com/secure"

def test_login_success():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(LOGIN_URL)

    usernameField = driver.find_element(By.ID, 'username')
    passwordField = driver.find_element(By.ID, 'password')
    submitButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button')

    usernameField.send_keys('tomsmith')
    passwordField.send_keys('SuperSecretPassword!')
    submitButton.click()

    assert(driver.current_url == SECURE_URL)
    loginSuccessBanner = driver.find_element(By.CLASS_NAME, 'success')
    assert(loginSuccessBanner.is_displayed)
    driver.quit()

def test_login_fail():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(LOGIN_URL)

    usernameField = driver.find_element(By.ID, 'username')
    passwordField = driver.find_element(By.ID, 'password')
    submitButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button')

    usernameField.send_keys('tomsmith')
    passwordField.send_keys('MANAMBGNYAWOK!!!')
    submitButton.click()

    assert(driver.current_url == LOGIN_URL)
    loginFailedBanner = driver.find_element(By.CLASS_NAME, 'error')
    assert(loginFailedBanner.is_displayed)
    driver.quit()
