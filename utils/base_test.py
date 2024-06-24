import json
import logging
import os
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        logger = logging.getLogger('UI Automate testing')
        logger.setLevel(logging.INFO)  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

        # Create a file handler that overwrites the log file each time
        file_handler = logging.FileHandler("log_info.log", mode='w')
        file_handler.setLevel(logging.INFO)

        # Create a logging format
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        # Add the file handler to the logger
        logger.addHandler(file_handler)
        return logger

    def get_test_case_data(self, tested_page, test_case, expected_result):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_directory, f"tests data/{tested_page}.json")
        with open(data_path, 'r') as file:
            test_data = json.load(file)

        return test_data[test_case][expected_result]
