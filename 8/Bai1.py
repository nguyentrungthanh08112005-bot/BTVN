import unittest

def calculate_tax(income):
    if income < 5000:
        return 0
    elif income < 10000:
        return income * 0.1
    else:
        return income * 0.2

class TestCalculateTax(unittest.TestCase):

    def test_income_low(self):
        # Trường hợp: income < 5000
        self.assertEqual(calculate_tax(3000), 0)

    def test_income_medium(self):
        # Trường hợp: income = 7000
        self.assertEqual(calculate_tax(7000), 700.0)

    def test_income_high(self):
        # Trường hợp: income = 12000
        self.assertEqual(calculate_tax(12000), 2400.0)

    def test_income_boundary_5000(self):
        # Test thêm trường hợp biên: income bằng 5000 (phải rơi vào nhánh < 10000)
        self.assertEqual(calculate_tax(5000), 500.0)

if __name__ == '__main__':
    unittest.main()