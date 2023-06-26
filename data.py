import csv, datetime


def get_test_case_from_file_OFF():
    try:
        with open('C:\\Users\\rrzeszotek\\PycharmProjects\\TestFramework\\tc_data.csv', 'r', encoding='utf-8') as rfile:
            csv_data = csv.DictReader(rfile, delimiter='|')
            for test_case in csv_data:
                tc_name = test_case['TCName']
                env = test_case['Enviroment']
                ver = test_case['App_ver']
                tc_data = test_case['data']
            return tc_name, env, ver, tc_data

    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)


def get_test_data(tc_data_list):
    tc_data_list = tc_data_list.split(',')
    data_dict = {}
    for i in tc_data_list:
        row_list = i.split(':')
        data_dict[row_list[0]] = row_list[1]
    return data_dict


def save_test_result(tc_name, test_result, expected_result):
    header = ['tc_name', 'test_result', 'expected_result', 'result']
    if test_result == expected_result:
        result = 'Passed'
    else:
        result = 'Failed'
    data = [tc_name, test_result, expected_result, result, datetime.datetime.now()]
    with open('C:\\Users\\rrzeszotek\\PycharmProjects\\TestFramework\\tc_results.csv', 'a', encoding='UTF8',
              newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_test_case_from_file(no_row):
    try:
        with open('C:\\Users\\rrzeszotek\\PycharmProjects\\TestFramework\\tc_data.csv', 'r', encoding='utf-8') as rfile:
            csv_data = csv.reader(rfile, delimiter='|')
            csv_data = list(csv_data)
            csv_data = csv_data[no_row]
            tc_name = csv_data[0]
            env = csv_data[1]
            ver = csv_data[2]
            tc_data = csv_data[3]
            return tc_name, env, ver, tc_data

    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)

def get_def_test_case_from_file(tc_name):
    try:
        with open('C:\\Users\\rrzeszotek\\PycharmProjects\\TestFramework\\tc_data.csv', 'r', encoding='utf-8') as rfile:
            csv_data = csv.DictReader(rfile, delimiter='|')
            index = 1
            list_row = []
            for test_case in csv_data:
                if test_case['TSName'] == tc_name:
                    row_num = index
                    list_row.append(row_num)
                index += 1
            return list_row



    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)

def get_number_of_row():
    try:
        with open('C:\\Users\\rrzeszotek\\PycharmProjects\\TestFramework\\tc_data.csv', 'r', encoding='utf-8') as rfile:
            return len(rfile.readlines())

    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)


#get_def_test_case_from_file('Login')
# tc_data = "login:admin,password:test"
# print(get_test_case_from_file(2))
# print(get_number_of_row())

# print(get_test_data(tc_data)['login'])

# print(tc_data['login'])
