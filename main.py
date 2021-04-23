from configurator import Configurator
from connector import Connector
from resulting import Result
from test_processor import TestProcessor


def run():
    # get configs. Instead "conf" you can use sys.argv[1] and set it in
    # parameters. E.g. it useful for splitting env. (dev / qa)
    config = Configurator("conf")
    logger = Result(config)
    connector = Connector(config, logger)
    test_processor = TestProcessor(config, connector, logger)
    test_processor.process()


if __name__ == '__main__':
    run()
