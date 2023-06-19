import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import run
import TestStep.login

driver = run.OpenBrowser()
driver = driver.open_browser()

login_page = TestStep.login.LoginPage()
expected_result = login_page.login_page()