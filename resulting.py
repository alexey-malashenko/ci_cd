import os
from datetime import datetime


class Result:
    def __init__(self, config):
        self.config = config
        self.check_log_file()
        self.result_file = open(f'{config.get_test_result_folder()}'
                                f'\\result.log', 'a')
        self.log_file = open(f'{config.get_test_result_folder()}'
                             f'\\log_file.log', 'a')

    def check_log_file(self):
        if os.path.exists(self.config.get_test_result_folder()):
            pass
        else:
            print('Wrong path to log file. Please check "test_result_folder" '
                  'in config.json')
            exit()

    def check_db_connection(self, res):
        if res:
            self.log_file.write(f'{datetime.now()}'
                                f' Database connection successful\n')
        else:
            self.log_file.write(f'{datetime.now()}'
                                f' Database connection failed. Please check '
                                f'"database_settings" in config.json\n')

    def print_message(self):
        print(f'Error. Please, check log by path: "'
              f'{os.path.join(self.config.get_test_data_folder())}"')
        self.close_all_files()

    def check_test_case(self, res):
        if res:
            self.log_file.write(f'{datetime.now()}'
                                f' Test cases folder detected\n')
        else:
            self.log_file.write(f'{datetime.now()}'
                                f' Test cases folder not detected. Please '
                                f'check "test_cases_folder" in config.json\n')

    def test_file_json(self, par, file_name):
        if par == 'empty':
            self.log_file.write(
                f'{datetime.now()}'
                f' Test cases script do not detected. Please '
                f'check '
                f'{os.path.join(self.config.get_test_data_folder())}\n')
        elif par == 'wrong json':
            self.log_file.write(
                f'{datetime.now()}'
                f' Wrong JSON file. Please check file {file_name}\n')
        elif par == 'good json':
            self.log_file.write(
                f'{datetime.now()}'
                f' {file_name} JSON was successfully opened.\n')
        elif par == 'wrong str':
            self.log_file.write(
                f'{datetime.now()}'
                f' Wrong structure of JSON file. Please check file '
                f'{file_name}\n')
        elif par == 'good str':
            self.log_file.write(
                f'{datetime.now()}'
                f' {file_name} '
                f'JSON file structure was successfully checked.\n')

    def start_test(self, file_name):
        self.log_file.write(f'{datetime.now()}'
                            f' Testing with "'
                            f'{os.path.basename(file_name)}" '
                            f'have been started\n')

    def finish_test(self, file_name):
        self.log_file.write(f'{datetime.now()}'
                            f' Testing with "'
                            f'{os.path.basename(file_name)}" '
                            f'have been completed\n')

    def start_case(self, test_name):
        self.log_file.write(f'{datetime.now()}'
                            f' Test case "'
                            f'{test_name}" '
                            f'have been started\n')

    def finish_case(self, test_name):
        self.log_file.write(f'{datetime.now()}'
                            f' Test case "'
                            f'{test_name}" '
                            f'have been completed\n')

    def check_tesult(self, res, test_name, actual_result, expected_result):
        if res:
            self.result_file.write(f'{datetime.now()}'
                                   f' PASSED. Test case "'
                                   f'{test_name}". '
                                   f'Result is: {actual_result}. '
                                   f'Expected result is: {expected_result}\n')
        else:
            self.result_file.write(f'{datetime.now()}'
                                   f' FAILED. Test case "'
                                   f'{test_name}". '
                                   f'Result is: {actual_result}. '
                                   f'Expected result is: {expected_result}\n')

    def close_all_files(self):
        self.log_file.write(f'{datetime.now()}'
                            f' Testing completed\n')
        self.result_file.close()
        self.log_file.close()
