import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from TestServices.Config.get_test_input import GetTestInput
from TestServices.AccessMethods.run_test_methods import RunTestMethods
from TestServices.Generic.verify_country import VerifyCountry

# Get test cofiguration input
config = GetTestInput(__file__)

# Run method to be tested
sql = RunTestMethods(config)
list_german_customers = sql.read_german_customers()
list_german_speaking_customers = sql.read_german_speaking_customers()
list_french_speaking_customers = sql.read_french_speaking_customers()


class TestClass:
    def test_001_german_customers(self):
        reference_list = ["Germany"]
        test_value = VerifyCountry.iterate_list(reference_list, list_german_customers)
        assert test_value

    def test_002_german_speaking_customers(self):
        reference_list = config.german_speaking_countries
        test_value = VerifyCountry.iterate_list(reference_list, list_german_speaking_customers)
        assert test_value

    def test_003_french_speaking_customers(self):
        reference_list = config.french_speaking_countries
        test_value = VerifyCountry.iterate_list(reference_list, list_french_speaking_customers)
        assert test_value
