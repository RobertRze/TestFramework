import run
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox import webdriver


#from TestCases.login import driver


class LoginPage:

    def __init__(self, login_name, password):
        self.el_input_login = "login"
        self.el_input_password = "password"
        self.btn_login = ".MuiButton-contained > .MuiButton-label"
        self.login, self.password = login_name, password
        self.expected_result = '/html/body/div[1]/div/form/p'

    def login_page(self, driver, mode):
        try:
            if mode == 'OK':
                self.login, self.password = run.get_user_to_login()
            driver.find_element(By.NAME, self.el_input_login).send_keys(self.login)
            driver.find_element(By.NAME, self.el_input_password).send_keys(self.password)
            driver.find_element(By.CSS_SELECTOR, self.btn_login).click()
            if mode == 'wrong':
                time.sleep(2)
                text2 = driver.find_element(By.XPATH, self.expected_result).text
                return text2
        except NoSuchElementException as err:
            return 'The element does not exist', err


