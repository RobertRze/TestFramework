# Generated by Selenium IDE
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


class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("http://10.10.252.161/clearanceslipApp/Stuffs")
        self.driver.set_window_size(1075, 1013)
        self.driver.
        self.driver.find_element(By.CSS_SELECTOR, ".jss430 .MuiButtonBase-root:nth-child(4) path").click()
        self.driver.find_element(By.CSS_SELECTOR, ".Mui-focused > .MuiInputBase-input").is_displayed()
        self.driver.find_element(By.CSS_SELECTOR, ".Mui-focused > .MuiInputBase-input").send_keys("Książka")
        self.driver.find_element(By.CSS_SELECTOR, ".Mui-focused > .MuiInputBase-input").send_keys("QA")
        self.driver.find_element(By.CSS_SELECTOR, ".jss667 > .MuiButton-label").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".jss668 .MuiSvgIcon-root")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".jss668 .MuiSvgIcon-root").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".jss667 > .MuiButton-label")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".jss666 .MuiSvgIcon-root")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".jss666 .MuiSvgIcon-root").click()
        self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-textPrimary:nth-child(1) > .MuiButton-label").click()