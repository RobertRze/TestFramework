import run
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException


# driver = webdriver.Firefox()
# driver.get('http://10.10.252.161/clearanceslipApp')
#
# driver.set_window_size(1457, 881)

class Items:

    def __init__(self, name, departament):
        self.item_name = '/html/body/div[1]/div/main/div/div[1]/form/div/div[1]/div/div/input'
        self.department = '//*[@id="demo-simple-select"]'
        self.department_value = 'QA'
        self.name = name
        self.departament = departament

    def add_item(self, driver):
        try:
            driver.find_element(By.XPATH, self.item_name).send_keys(self.name)
            driver.find_element(By.XPATH, self.departament).click()
            driver.find_element(By.NAME, self.departament).click()

        except NoSuchElementException as err:
            return 'The element does not exist', err
