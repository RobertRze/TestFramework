import run
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox import webdriver
from selenium import webdriver


class LeftMenu:

    def __init__(self):
        self.items = '/html/body/div[1]/div/div/div/div/ul[6]/div/div[2]/span'

    def left_menu(self, driver, menu):
        try:
            time.sleep(2)
            if menu == 'Items':
                driver.find_element(By.XPATH, self.items).click()

        except NoSuchElementException as err:
            return 'The element does not exist', err
