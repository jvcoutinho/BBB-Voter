import json

from selenium import webdriver


def read_configuration_file():
    with open('config.json') as file:
        arguments = json.load(file)
    return arguments

arguments = read_configuration_file()

driver = webdriver.Edge(executable_path='./msedgedriver.exe')
driver.get(arguments['pollURL'])
driver.find_elements_by_xpath("//*[contains(text()," + arguments['target'] + ")]")
