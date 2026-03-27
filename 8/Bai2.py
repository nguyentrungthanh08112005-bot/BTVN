import unittest

def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):

    def test_prime_numbers(self):
        # Các số nguyên tố mong đợi trả về True
        self.assertTrue(is_prime(2), "Số 2 phải là số nguyên tố")
        self.assertTrue(is_prime(3), "Số 3 phải là số nguyên tố")
        self.assertTrue(is_prime(17), "Số 17 phải là số nguyên tố")
        self.assertTrue(is_prime(19), "Số 19 phải là số nguyên tố")

    def test_non_prime_numbers(self):
        # Các số không phải số nguyên tố mong đợi trả về False
        self.assertFalse(is_prime(1), "Số 1 không phải là số nguyên tố")
        self.assertFalse(is_prime(4), "Số 4 không phải là số nguyên tố")
        self.assertFalse(is_prime(18), "Số 18 không phải là số nguyên tố")

    def test_negative_numbers(self):
        # Kiểm tra thêm trường hợp số âm
        self.assertFalse(is_prime(-5), "Số âm không thể là số nguyên tố")

if __name__ == '__main__':
    unittest.main()