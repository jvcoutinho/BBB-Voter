import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def read_configuration_file():
    with open('config.json') as file:
        arguments = json.load(file)
    return arguments

def create_tab(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

def close_tab(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

def login(driver, email, password):
    create_tab(driver)
    driver.get('https://login.globo.com/login/1')
    
    email_input = driver.find_element_by_name('login')
    password_input = driver.find_element_by_name('password')
    form = driver.find_element_by_id('login-form')

    email_input.send_keys(email)
    password_input.send_keys(password)
    form.submit()
    
    close_tab(driver)

arguments = read_configuration_file()

print("You're voting on", arguments['target'])

driver = webdriver.Edge(executable_path='./msedgedriver.exe')

login(driver, arguments['credentials']['username'],
      arguments['credentials']['password'])

driver.get(arguments['pollURL'])

# target = driver.find_element_by_xpath(
#     "//div[text()='" + arguments['target'] + "']//ancestor::div")

# target.click()

driver.close()
