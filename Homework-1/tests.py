import unittest
from credit_card_validator import credit_card_validator

class TestCreditCardValidator(unittest.TestCase):

    def test11(self):
        """Verifies if Master Cards with valid lengths and invalid check bits returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("...."))

if __name__ == "__main__":
    unittest.main()
