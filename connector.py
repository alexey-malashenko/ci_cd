import pyodbc


class Connector:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.check_connection()
        conn = pyodbc.connect(self.config.get_database_settings())
        self.cursor = conn.cursor()

    def check_connection(self):
        try:
            pyodbc.connect(self.config.get_database_settings())
        except (ValueError, Exception):
            self.logger.check_db_connection(False)
            self.logger.print_message()
            exit()
        else:
            self.logger.check_db_connection(True)

        # self.cursor.execute('SELECT * FROM hr.jobs')
        #
        # for row in self.cursor:
        #     print(row)

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
