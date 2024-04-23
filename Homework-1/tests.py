import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    def test0(self):
        """Verifies if an empty credit card returns False."""
        self.assertFalse(credit_card_validator(""))

    def test1(self):
        """Verifies if Visa cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("4012340123401234"))

    def test2(self):
        """Verifies if Visa cards with valid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("5012340123401205"))

    def test3(self):
        """Verifies if Visa cards with invalid lengths and valid prefixes returns False."""
        self.assertFalse(credit_card_validator("40123401234123006"))

    def test4(self):
        """Verifies if Visa cards with invalid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("701234012340003"))

    def test5(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5112340123401204"))

    def test6(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5212340123401203"))

    def test7(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5312340123401202"))

    def test8(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5412340123401201"))

    def test9(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("5512340123401200"))

    def test10(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2221123412341234"))

    def test11(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2221123412341207"))

    def test12(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2720123412341203"))

    def test13(self):
        """Verifies if MasterCard cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("2500123412341209"))

    def test14(self):
        """Verifies if MasterCard cards with invalid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("59123401234"))

    def test15(self):
        """Verifies if American Express cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("341234012340108"))

    def test16(self):
        """Verifies if American Express cards with valid lengths and valid prefixes returns True."""
        self.assertTrue(credit_card_validator("371234012340101"))

    def test17(self):
        """Verifies if American Express cards with valid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("321234012340102"))

    def test18(self):
        """Verifies if American Express cards with invalid lengths and valid prefixes returns False."""
        self.assertFalse(credit_card_validator("341234012340123401234"))

    def test19(self):
        """Verifies if American Express cards with invalid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("39123401234302"))

    def test20(self):
        """Verifies if Visa cards have non-numeric characters returns False."""
        self.assertFalse(credit_card_validator("4042318abc171915"))

    def test21(self):
        """Verifies if Visa cards have non-numeric characters returns False."""
        self.assertFalse(credit_card_validator("4042-3180-3147-1915"))

    def test22(self):
        """Verifies if Visa cards have white space in between numbers returns False."""
        self.assertFalse(credit_card_validator("4042 3180 3147 1915"))

    def test23(self):
        """Verifies if Visa cards have white space before numbers returns False."""
        self.assertFalse(credit_card_validator("    4042318031471915"))

    def test24(self):
        """Verifies if Visa cards have white space after numbers returns False."""
        self.assertFalse(credit_card_validator("4042318031471915     "))

    def test25(self):
        """Verifies if Visa cards with valid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("3012340123401234"))

    def test26(self):
        """Verifies if Visa cards with invalid lengths and valid prefixes returns False."""
        self.assertFalse(credit_card_validator("40123401234642869"))

    def test27(self):
        """Verifies Visa card edge cases if valid returns True."""
        self.assertTrue(credit_card_validator("4000123412341234"))
        
    def test28(self):
        """Verifies Visa card edge cases if valid returns True."""
        self.assertTrue(credit_card_validator("4999123412341203"))

    def test29(self):
        """Verifies if MasterCard cards with non-numeric characters return False."""
        self.assertFalse(credit_card_validator("511234abc5678901"))

    def test30(self):
        """Verifies if MasterCard cards with whitespace return False."""
        self.assertFalse(credit_card_validator("5112 3456 7890 1234"))

    def test31(self):
        """Verifies if MasterCard cards with whitespace before numbers return False."""
        self.assertFalse(credit_card_validator("    5112345678901234"))

    def test32(self):
        """Verifies if MasterCard cards with whitespace after numbers return False."""
        self.assertFalse(credit_card_validator("5112345678901234     "))

    def test33(self):
        """Verifies if MasterCard cards with invalid prefixes return False."""
        self.assertFalse(credit_card_validator("6012345678901234"))

    def test34(self):
        """Verifies if MasterCard cards with invalid lengths return False."""
        self.assertFalse(credit_card_validator("551234567890106"))

    def test35(self):
        """Verifies if MasterCard cards with invalid lengths return False."""
        self.assertFalse(credit_card_validator("55123456789012309"))

    def test36(self):
        """Verifies MasterCard edge cases if valid return True."""
        self.assertTrue(credit_card_validator("5112345678901201"))
    
    def test37(self):
        """Verifies MasterCard edge cases if valid return True."""
        self.assertTrue(credit_card_validator("5599123456789003"))

    def test38(self):
        """Verifies if American Express cards with non-numeric characters return False."""
        self.assertFalse(credit_card_validator("371234abc567890"))

    def test39(self):
        """Verifies if American Express cards with whitespace return False."""
        self.assertFalse(credit_card_validator("3712 345678 90123"))

    def test40s(self):
        """Verifies if American Express cards with whitespace before numbers return False."""
        self.assertFalse(credit_card_validator("    371234567890123"))

    def test41(self):
        """Verifies if American Express cards with whitespace after numbers return False."""
        self.assertFalse(credit_card_validator("371234567890123     "))

    def test42(self):
        """Verifies if American Express cards with invalid prefixes return False."""
        self.assertFalse(credit_card_validator("321234567890123"))

    def test43(self):
        """Verifies if American Express cards with invalid lengths return False."""
        self.assertFalse(credit_card_validator("37123456789012"))

    def test44(self):
        """Verifies if American Express cards with invalid lengths return False."""    
        self.assertFalse(credit_card_validator("3712345678901200"))

    def test45(self):
        """Verifies American Express edge case with minimum valid length."""
        self.assertTrue(credit_card_validator("341234567890101"))

    def test46(self):
        """Verifies American Express edge case with maximum valid length."""
        self.assertTrue(credit_card_validator("379912345678907"))

    def test47(self):
        """Verifies if American Express cards with invalid checksums return False."""
        self.assertFalse(credit_card_validator("378282246310105"))

    def test48(self):
        """Verifies if MasterCard cards with invalid checksums return False."""
        self.assertFalse(credit_card_validator("5555555555554444"))

    def test49(self):
        """Verifies if Visa cards with invalid checksums return False."""
        self.assertFalse(credit_card_validator("4111111111111111"))

    def test50(self):
        """Verifies if American Express cards with valid checksums return True."""
        self.assertTrue(credit_card_validator("378282246310005"))

    def test51(self):
        """Verifies if MasterCard cards with valid checksums return True."""
        self.assertTrue(credit_card_validator("5555555555554444"))

    def test52(self):
        """Verifies if Visa cards with valid checksums return True."""
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test53(self):
        """Verifies if American Express cards with valid Luhn algorithm return True."""
        self.assertTrue(credit_card_validator("378282246310005"))

    def test54(self):
        """Verifies if MasterCard cards with valid Luhn algorithm return True."""
        self.assertTrue(credit_card_validator("5555555555554444"))

    def test55(self):
        """Verifies if Visa cards with valid Luhn algorithm return True."""
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test56(self):
        """Verifies if American Express cards with invalid Luhn algorithm return False."""
        self.assertFalse(credit_card_validator("378282246310006"))

    def test57(self):
        """Verifies if MasterCard cards with invalid Luhn algorithm return False."""
        self.assertFalse(credit_card_validator("5555555555554445"))

    def test58(self):
        """Verifies if Visa cards with invalid Luhn algorithm return False."""
        self.assertFalse(credit_card_validator("4111111111111112"))
    
    def test59(self):
        """Verifies if Visa cards with invalid length return False."""
        self.assertFalse(credit_card_validator("423456789012344"))

    def test59(self):
        """Verifies if Visa cards with invalid length return False."""
        self.assertFalse(credit_card_validator("42345678901234566"))

    def test60(self):
        """Verifies if MasterCard cards with invalid length return False."""
        self.assertFalse(credit_card_validator("27200401234120906"))

    def test61(self):
        """Verifies if MasterCard cards with valid length return True."""
        self.assertTrue(credit_card_validator("5534567890123450"))
    
    def test62(self):
        """Verifies if MasterCard cards with valid length return True."""
        self.assertTrue(credit_card_validator("2221567890123455"))

    def test63(self):
        """Verifies if MasterCard cards with valid length return True."""
        self.assertTrue(credit_card_validator("2720567890123451"))

    def test64(self):
        """Verifies if MasterCard cards with valid length return True."""
        self.assertTrue(credit_card_validator("2222567890123454"))

    def test65(self):
        """Verifies if Visa cards with valid length return True."""
        self.assertTrue(credit_card_validator("4015695121783007"))

    def test66(self):
        """Verifies if Visa cards with valid length return True."""
        self.assertTrue(credit_card_validator("4995695121783001"))

    def test67(self):
        """Verifies if cards with special characters return False."""
        self.assertFalse(credit_card_validator("!%15695121783007"))

    def test67(self):
        """Verifies if Visa cards with same characters return False."""
        self.assertFalse(credit_card_validator("4444444444444444"))

    def test68(self):
        """Verifies if American Express cards with invalid length return False."""
        self.assertFalse(credit_card_validator("37123456789012"))

    def test68(self):
        """Verifies if American Express cards with invalid length return False."""
        self.assertFalse(credit_card_validator("3712345678901234"))

    def test69(self):
        """Verifies if MasterCard cards with valid lengths and invalid prefixes returns False."""
        self.assertFalse(credit_card_validator("5912340123401206"))

    def test70(self):
        """Verifies if MasterCard cards with invalid lengths and valid prefixes returns False."""
        self.assertFalse(credit_card_validator("511234012341209"))

    def test71(self):
        """Verifies if MasterCard cards with invalid lengths and valid prefixes returns False."""
        self.assertFalse(credit_card_validator("55123401234120901"))

    def test72(self):
        """Verifies if MasterCard cards with invalid length return False."""
        self.assertFalse(credit_card_validator("22210040123412005"))

    def test73(self):
        """Verifies if American Express cards with invalid length return False."""
        self.assertFalse(credit_card_validator("34123456789007"))

    def test74(self):
        """Verifies if American Express cards with invalid length return False."""
        self.assertFalse(credit_card_validator("3412345678901203"))

if __name__ == "__main__":
    unittest.main()
