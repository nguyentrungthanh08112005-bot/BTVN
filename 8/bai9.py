import unittest

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

class TestSafeDivide(unittest.TestCase):

    def test_divide_positive(self):
        # Trường hợp: 10 / 2 = 5.0
        self.assertEqual(safe_divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        # Trường hợp: chia cho 0 phải trả về None
        self.assertIsNone(safe_divide(5, 0), "Chia cho 0 phải trả về None")

    def test_divide_negative(self):
        # Trường hợp: -4 / 2 = -2.0
        self.assertEqual(safe_divide(-4, 2), -2.0)

    def test_divide_float(self):
        # Test thêm trường hợp số thập phân
        self.assertEqual(safe_divide(5, 2), 2.5)

if __name__ == '__main__':
    unittest.main()