from selenium.common import NoSuchElementException

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
from selenium.webdriver.support.select import Select


# driver = webdriver.Firefox()
# driver.get('http://10.10.252.161/clearanceslipApp')
#
# driver.set_window_size(1457, 881)

class Position:

    def __init__(self, position_value):
        self.position_name = 'positionName'
        self.btn_Dodaj = '/html/body/div[1]/div/main/div/div[1]/form/div[3]/label/span[1]'
        self.position_value = position_value

    def add_position(self, driver):
        try:
            driver.find_element(By.NAME, self.position_name).send_keys(self.position_value)
            driver.find_element(By.XPATH, self.btn_Dodaj).click()
            result = driver.find_element(By.ID, 'client-snackbar').text
            return result
        except NoSuchElementException as err:
            return 'The element does not exist', err



    def find_position(self, driver, mode):
        try:
            for i in range(2, 11):
                position_name_list = driver.find_element(By.CSS_SELECTOR,
                                                         f".MuiTableRow-root:nth-child({i}) > .MuiTableCell-root:nth-child(2)").text
                if position_name_list == self.position_value:
                    if mode == 'delete':
                        driver.find_element(By.CSS_SELECTOR, f".MuiTableRow-root:nth-child({i}) .MuiSvgIcon-root").click()
                        driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) > .MuiButton-label").click()
                        result = driver.find_element(By.ID, 'client-snackbar').text
                        return result
                    elif mode == 'edit':
                        driver.find_element(By.CSS_SELECTOR,
                                            f".MuiTableRow-root:nth-child({i}) .MuiButton-label").click()
                        self.position_value = self.position_value + '01'
                        driver.find_element(By.CSS_SELECTOR, ".MuiInput-input").clear()
                        driver.find_element(By.CSS_SELECTOR, ".MuiInput-input").send_keys(self.position_value)
                        time.sleep(2)
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div[2]/table/tbody/tr[{i}]/td[3]/div/button[1]/span[1]').click()
                        result = driver.find_element(By.ID, 'client-snackbar').text
                        return result
                    break
        except NoSuchElementException as err:
            return 'The element does not exist', err

