import os
import json
from jsonschema import validate
import glob


class TestProcessor:
    def __init__(self, config, connector, logger):
        self.config = config
        self.connector = connector
        self.logger = logger
        self.validate_test_case_folder()
        self.validate_test_file_json()

    def validate_test_case_folder(self):
        if os.path.exists(self.config.get_test_data_folder()):
            self.logger.check_test_case(True)
        else:
            self.logger.check_test_case(False)
            self.logger.print_message()
            exit()

    def validate_test_file_json(self):
        # if exists
        test_data_files = self.check_test_folder()
        if not test_data_files:
            self.logger.test_file_json('empty', '')
            self.logger.print_message()
            exit()

        for f in test_data_files:
            try:
                fl = open(f, 'r')
                json.load(fl)
            except (ValueError, Exception):
                self.logger.test_file_json('wrong json', f)
                self.logger.print_message()
                exit()
            else:
                self.logger.test_file_json('good json', f)

        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "query": {
                    "type": "string"
                },
                "expected": {
                    "type": "integer"
                }
            },
            "required": [
                "name",
                "query",
                "expected"
            ]
        }

        for f in test_data_files:
            try:
                fl = open(f, 'r')
                json_file = json.load(fl)
                for ar in json_file:
                    if ar == 'tests':
                        for test_case in json_file[ar]:
                            validate(instance=test_case,
                                     schema=schema)
                    else:
                        self.logger.test_file_json('wrong str', f)
                        self.logger.print_message()
                        exit()
            except (ValueError, Exception):
                self.logger.test_file_json('wrong str', f)
                self.logger.print_message()
                exit()
            else:
                self.logger.test_file_json('good str', f)

    def check_test_folder(self):
        test_data_folder = self.config.get_test_data_folder()
        return [f for f in glob.glob(test_data_folder + '/*.json',
                                     recursive=True)]

    def process(self):
        test_data_files = self.check_test_folder()
        for f in test_data_files:
            self.do_testing(f)

        self.logger.close_all_files()

    def do_testing(self, file_name):
        self.logger.start_test(file_name)
        test_data = self.read_test_data_file(file_name)
        for test in test_data['tests']:
            self.logger.start_case(test['name'])
            query = test['query']
            expected_result = test['expected']
            actual_result = self.connector.execute(query)
            if actual_result == expected_result:
                self.logger.check_tesult(True, test['name'], actual_result,
                                         expected_result)
            else:
                self.logger.check_tesult(False, test['name'], actual_result,
                                         expected_result)
            self.logger.finish_case(test['name'])
        self.logger.finish_test(file_name)

    # noinspection PyMethodMayBeStatic
    def read_test_data_file(self, file_name):
        with open(file_name) as f:
            test_data = json.load(f)
        return test_data
