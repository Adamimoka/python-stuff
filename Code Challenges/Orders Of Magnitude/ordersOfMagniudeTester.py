import unittest
from ordersOfMagnitude import ordersOfMagnitude
class TestOrdersOfMagnitude(unittest.TestCase):
    def test_orders_of_magnitude_1(self):
        self.assertEqual(ordersOfMagnitude("3.2 thousand"), 3200)

    def test_orders_of_magnitude_2(self):
        self.assertEqual(ordersOfMagnitude("7.1 thousand"), 7100)

    def test_orders_of_magnitude_3(self):
        self.assertEqual(ordersOfMagnitude("81.23 hundred"), 8123)

    def test_orders_of_magnitude_4(self):
        self.assertEqual(ordersOfMagnitude("95.4 hundred"), 9540)

    def test_orders_of_magnitude_5(self):
        self.assertEqual(ordersOfMagnitude("0.451 million"), 451000)

    def test_orders_of_magnitude_6(self):
        self.assertEqual(ordersOfMagnitude("1.39 million"), 1390000)

    def test_orders_of_magnitude_7(self):
        self.assertEqual(ordersOfMagnitude("99.999 million"), 99999000)

    def test_orders_of_magnitude_8(self):
        self.assertEqual(ordersOfMagnitude("99.987 million"), 99987000)
    
if __name__ == "__main__":
    unittest.main()