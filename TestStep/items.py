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


class Items:

    def __init__(self, name, departament):
        self.item_name = '/html/body/div[1]/div/main/div/div[1]/form/div/div[1]/div/div/input'
        self.department = '#demo-simple-select'
        self.department_value = departament
        self.name = name

    def add_item(self, driver):
        try:
            driver.find_element(By.XPATH, self.item_name).send_keys(self.name)
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, self.department).click()
            for i in range(1, 10):
                department_name = driver.find_element(By.XPATH, f"//div[@id=\'menu-teamId\']/div[3]/ul/li[{i}]").text
                if department_name == self.department_value:
                    driver.find_element(By.XPATH, f"//div[@id=\'menu-teamId\']/div[3]/ul/li[{i}]").click()
                    time.sleep(2)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[1]/form/div/div[5]/label").click()
                    result = driver.find_element(By.ID, 'client-snackbar').text
                    return result
                    break
            # departament_list.send_keys(self.department_value)
        except NoSuchElementException as err:
            return 'The element does not exist', err

    def search_item(self, driver, mode):
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[1]/div/button[2]").click()
            if mode == 'delete':
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[1]/div/button[2]").click()
            driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/ul/li[1]/div/div/div/input").send_keys(self.name)
            driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/ul/li[2]/div/div/div/input").send_keys(self.department_value)
            time.sleep(2)
            if mode == 'edit':
                driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/table/tbody/tr/td[4]/button").click()
                self.name = self.name + '01'
                driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/table/tbody/tr/td[2]/div/div/input").clear()
                driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/table/tbody/tr/td[2]/div/div/input").send_keys(self.name)
                driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/table/tbody/tr/td[4]/div/button[1]/span[1]").click()
            elif mode == 'delete':
                driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/table/tbody/tr/td[5]/button/span[1]").click()
                driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) > .MuiButton-label").click()
            result = driver.find_element(By.ID, 'client-snackbar').text
            return result

        except NoSuchElementException as err:
            return 'The element does not exist', err

