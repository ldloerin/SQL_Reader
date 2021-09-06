import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from TestServices.Config.get_test_input import GetTestInput
# from TestServices.AccessMethods.run_table_methods import RunTableMethods

# Get test cofiguration input
config = GetTestInput(__file__)

# Run method to be tested
# input = RunTableMethods(config)


class TestClass:
    def test_001_initialize_table(self):
        assert 1 == 1
