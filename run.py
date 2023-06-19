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


class OpenBrowser:
    def __init__(self):
        self.url = "http://10.10.252.161/clearanceslipApp"

    def open_browser(self):
        driver = webdriver.Firefox()
        driver.get(self.url)
        driver.set_window_size(1457, 881)
        return driver


def get_user_to_login():

    try:
        with open("C:/Users/rrzeszotek/PycharmProjects/TestFramework/credential.txt", encoding='utf-8') as file:
            data = file.read().split(',')
            return data[0], data[1]
    except FileNotFoundError:
        print("Nie ma takiego pliku")
        return None

