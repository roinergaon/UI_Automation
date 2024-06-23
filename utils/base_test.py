import json
import os
import sys

import pytest
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_test_case_data(self, test_case, expected_result):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_directory, 'test_data.json')
        with open(data_path, 'r') as file:
            test_data = json.load(file)

        return test_data[test_case][expected_result]
