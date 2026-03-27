import unittest
from unittest.mock import patch, io

def send_welcome_email(email):
    print(f"Sending email to {email}")

class TestEmailService(unittest.TestCase):

    # Sử dụng context manager 'patch' để mock hàm print hệ thống
    @patch('builtins.print')
    def test_send_welcome_email_calls_print(self, mock_print):
        # 1. Thiết lập dữ liệu giả định
        test_email = "test@example.com"
        expected_output = f"Sending email to {test_email}"

        # 2. Gọi hàm cần test
        send_welcome_email(test_email)

        # 3. Kiểm tra xem print() có được gọi hay không
        mock_print.assert_called()

        # 4. Kiểm tra xem nội dung in ra có đúng như mong đợi không
        mock_print.assert_called_with(expected_output)

    @patch('builtins.print')
    def test_send_welcome_email_multiple_calls(self, mock_print):
        # Kiểm tra khi gọi nhiều lần
        emails = ["user1@test.com", "user2@test.com"]
        for e in emails:
            send_welcome_email(e)
            
        # Xác nhận print được gọi đúng 2 lần
        self.assertEqual(mock_print.call_count, 2)

if __name__ == '__main__':
    unittest.main()