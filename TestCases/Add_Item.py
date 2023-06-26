import run, data, TestStep.login, TestStep.left_menu, TestStep.items
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


list_test_to_run = data.get_def_test_case_from_file('AddItem')
for i in list_test_to_run:

    tc_name, env, ver, tc_data = data.get_test_case_from_file(i)
    print(tc_name, env, ver)

    driver = run.OpenBrowser()
    driver = driver.open_browser()

    login = TestStep.login.LoginPage(data.get_test_data(tc_data)['login'], data.get_test_data(tc_data)['password'])
    login.login_page(driver, 'OK')

    left_menu = TestStep.left_menu.LeftMenu()
    left_menu.left_menu(driver, 'Items')

    items = TestStep.items.Items(data.get_test_data(tc_data)['item_name'], data.get_test_data(tc_data)['item_departament'])
    items.add_item(driver)

#    driver.close()