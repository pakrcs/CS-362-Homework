import unittest
import random
import string
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    pass


def build_test_func(test_case, func_under_test):

    def test(self):

        result = func_under_test(test_case)
        self.assertIsInstance(result, bool, 'The credit card number is valid: '+ str(result))

    return test


def generate_testcases(tests_to_generate=450000):
    for i in range(tests_to_generate):
        length = random.randint(14, 17)
        card_number = ''.join(random.choices(string.digits, k=length))

        test_func_name = 'test_' + str(i)
        test_case_func = build_test_func(card_number, credit_card_validator)
        setattr(TestCase, test_func_name, test_case_func)


if __name__ == '__main__':
    generate_testcases()
    unittest.main()
