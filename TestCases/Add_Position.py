import run, data, TestStep.login, TestStep.left_menu, TestStep.position
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


list_test_to_run = data.get_def_test_case_from_file('AddPosition')
for i in list_test_to_run:

    tc_name, env, ver, tc_data = data.get_test_case_from_file(i)
    print(tc_name, env, ver)

    driver = run.OpenBrowser()
    driver = driver.open_browser()

    login = TestStep.login.LoginPage(data.get_test_data(tc_data)['login'], data.get_test_data(tc_data)['password'])
    login.login_page(driver, 'OK')

    left_menu = TestStep.left_menu.LeftMenu()
    left_menu.left_menu(driver, 'position')

    position = TestStep.position.Position(data.get_test_data(tc_data)['position_name'])
    result_add = position.add_position(driver)
    data.save_test_result(tc_name, result_add, data.get_test_data(tc_data)['expected_result'])
    result_edit = position.find_position(driver, 'edit')
    data.save_test_result(tc_name, result_edit, data.get_test_data(tc_data)['expected_result_edit'])
    result_delete = position.find_position(driver, 'delete')
    data.save_test_result(tc_name, result_delete, data.get_test_data(tc_data)['expected_result_delete'])

    left_menu.left_menu(driver, 'logout')
    driver.close()