import os
import json


class Configurator:
    # I left env as a parameter so as not to forget how it can be used
    # in the future
    def __init__(self, env):
        self.read_config_file()
        self.directory = os.path.dirname(__file__)
        self.config = self.config[env]

    def read_config_file(self):
        with open('config.json') as f:
            self.config = json.load(f)

    def get_database_settings(self):
        return self.config['database_settings']

    def get_test_data_folder(self):
        return os.path.join(self.directory, self.config['test_cases_folder'])

    def get_test_result_folder(self):
        return os.path.join(self.directory, self.config['test_result_folder'])
