import unittest

class User:
    def __init__(self, username):
        self.username = username

    def is_admin(self):
        return self.username == "admin"

class TestUser(unittest.TestCase):

    def test_admin_user(self):
        # Trường hợp: username là 'admin'
        user = User("admin")
        self.assertTrue(user.is_admin(), "Username 'admin' phải có quyền admin")

    def test_guest_user(self):
        # Trường hợp: username là 'guest'
        user = User("guest")
        self.assertFalse(user.is_admin(), "Username 'guest' không được là admin")

    def test_random_user(self):
        # Trường hợp: username là 'user123'
        user = User("user123")
        self.assertFalse(user.is_admin(), "Username 'user123' không được là admin")

    def test_case_sensitivity(self):
        # Kiểm tra tính nhạy cảm với chữ hoa/chữ thường (Bonus)
        user = User("Admin")
        self.assertFalse(user.is_admin(), "Username 'Admin' (chữ hoa) không nên là admin")

if __name__ == '__main__':
    unittest.main()