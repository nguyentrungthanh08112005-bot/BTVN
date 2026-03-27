import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

def is_weekend():
    # .weekday() trả về: 0 (Thứ 2) -> 6 (Chủ nhật)
    # Thứ 7 là 5, Chủ nhật là 6
    today = datetime.now().weekday()
    return today >= 5

class TestIsWeekend(unittest.TestCase):

    @patch('__main__.datetime')
    def test_is_weekend_friday(self, mock_datetime):
        # 1. Giả lập hôm nay là Thứ 6 (weekday = 4)
        # Tạo một đối tượng mock cho ngày cụ thể: ví dụ 2023-10-27 là Thứ 6
        mock_date = MagicMock()
        mock_date.weekday.return_value = 4
        mock_datetime.now.return_value = mock_date

        # 2. Kiểm tra kết quả
        self.assertFalse(is_weekend(), "Thứ 6 không phải là cuối tuần")

    @patch('__main__.datetime')
    def test_is_weekend_saturday(self, mock_datetime):
        # 1. Giả lập hôm nay là Thứ 7 (weekday = 5)
        mock_date = MagicMock()
        mock_date.weekday.return_value = 5
        mock_datetime.now.return_value = mock_date

        # 2. Kiểm tra kết quả
        self.assertTrue(is_weekend(), "Thứ 7 phải là cuối tuần")

if __name__ == '__main__':
    unittest.main()