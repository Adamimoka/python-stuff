import unittest
from powerRule import powerRule
class TestPowerRule(unittest.TestCase):
    def test_power_rule_1(self):
        self.assertEqual(powerRule("4x^4+2x^3"), "16x^3+6x^2")

    def test_power_rule_2(self):
        self.assertEqual(powerRule("x^5+x^4"), "5x^4+4x^3")

    def test_power_rule_3(self):
        self.assertEqual(powerRule("3x^2+x+5"), "6x+1")

    def test_power_rule_4(self):
        self.assertEqual(powerRule("415"), "0")

    def test_power_rule_5(self):
        self.assertEqual(powerRule("3x^10+3x^9+3x^8+3x^7+3x^6+3x^5+3x^4"), "30x^9+27x^8+24x^7+21x^6+18x^5+15x^4+12x^3")

    def test_power_rule_6(self):
        self.assertEqual(powerRule("x^5+2x^2+3x+4"), "5x^4+4x+3")
    
if __name__ == "__main__":
    unittest.main()