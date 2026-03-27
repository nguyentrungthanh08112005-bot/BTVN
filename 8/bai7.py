import unittest

def is_strong(password):
    # Điều kiện: Ít nhất 8 ký tự VÀ có ít nhất 1 chữ số
    return len(password) >= 8 and any(c.isdigit() for c in password)

class TestPasswordStrength(unittest.TestCase):

    def test_strong_password(self):
        # Thỏa mãn cả 2 điều kiện
        self.assertTrue(is_strong("SecureP@ss123"))
        self.assertTrue(is_strong("12345678")) # Vừa đủ 8 ký tự và có số

    def test_weak_password_too_short(self):
        # Có số nhưng độ dài < 8
        self.assertFalse(is_strong("Pass1"), "Mật khẩu quá ngắn (5 ký tự) phải trả về False")
        self.assertFalse(is_strong("1234567"), "Mật khẩu 7 ký tự phải trả về False")

    def test_weak_password_no_digit(self):
        # Độ dài >= 8 nhưng không có số
        self.assertFalse(is_strong("VeryLongPassword"), "Mật khẩu không có số phải trả về False")
        self.assertFalse(is_strong("alphabetic"), "Mật khẩu chỉ có chữ cái phải trả về False")

    def test_empty_password(self):
        # Trường hợp rỗng
        self.assertFalse(is_strong(""))

if __name__ == '__main__':
    unittest.main()