class VerifyCountry:
    def iterate_list(reference_list, test_list):
        test_value = True
        for customer in test_list[1:]:
            customer = customer.split(",")
            if customer[-1] not in reference_list:
                test_value = False
                break
        return test_value
