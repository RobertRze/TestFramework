import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import run
from TestCases.login import driver


class LoginPage:
    def __init__(self):
        self.el_input_login = "login"
        self.el_input_password = "password"
        self.btn_login = ".MuiButton-contained > .MuiButton-label"
        self.login, self.password = run.get_user_to_login()
        self.expected_result = '/html/body/div[1]/div/form/p'

    def login_page(self):
        try:
            driver.find_element(By.NAME, "login").send_keys(self.login)
            driver.find_element(By.NAME, "password").send_keys(self.password)
            driver.find_element(By.CSS_SELECTOR, ".MuiButton-contained > .MuiButton-label").click()
            time.sleep(2)
            text2 = driver.find_element(By.XPATH, self.expected_result).text
            return text2
        except NoSuchElementException as err:
            return 'The element does not exist', err

