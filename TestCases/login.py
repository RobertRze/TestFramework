import run, data, TestStep.login
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


list_test_to_run = data.get_def_test_case_from_file('Login')
for i in list_test_to_run:

    tc_name, env, ver, tc_data = data.get_test_case_from_file(i)
    print(tc_name, env, ver)

    driver = run.OpenBrowser()
    driver = driver.open_browser()

    login = TestStep.login.LoginPage(data.get_test_data(tc_data)['login'], data.get_test_data(tc_data)['password'])
    test_result = login.login_page(driver, 'wrong')
    data.save_test_result(tc_name, test_result, data.get_test_data(tc_data)['expected_result'])

    driver.close()