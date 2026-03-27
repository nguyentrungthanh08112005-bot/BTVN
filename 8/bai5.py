import unittest
from unittest.mock import patch, MagicMock
import requests

def fetch_user():
    response = requests.get("https://api.example.com/user")
    return response.json()

class TestFetchUser(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_user_success(self, mock_get):
       
        expected_user_data = {"id": 1, "name": "Gemini AI", "role": "Collaborator"}

     
        mock_response = MagicMock()
        mock_response.json.return_value = expected_user_data
        
        mock_get.return_value = mock_response

        result = fetch_user()

        self.assertEqual(result, expected_user_data)
        
        mock_get.assert_called_once_with("https://api.example.com/user")

    @patch('requests.get')
    def test_fetch_user_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
    
        fetch_user()
        mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()