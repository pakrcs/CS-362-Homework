import unittest
from credit_card_validator import credit_card_validator

class TestCreditCardValidator(unittest.TestCase):

    def test1(self):
        """Verifies if Visa cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("4012340123401234"))

    def test2(self):
        """Verifies if Visa cards with valid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("7012340123401234"))

    def test3(self):
        """Verifies if Visa cards with invalid lengths and valid prefixes returns False."""
        self.assertFalse(credit_card_validator("40123401234"))

    def test4(self):
        """Verifies if Visa cards with invalid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("701234012340"))

    def test5(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5112340123401234"))

    def test6(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5212340123401234"))

    def test7(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5312340123401234"))

    def test8(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5412340123401234"))

    def test9(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5512340123401234"))

    def test10(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2221123412341234"))

    def test11(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2221123412341234"))

    def test12(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2720123412341234"))

    def test13(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2500123412341234"))

if __name__ == "__main__":
    unittest.main()
