import unittest

def clean_input(s):

    return s.strip().lower().replace(" ", "_")

class TestCleanInput(unittest.TestCase):

    def test_basic_cleaning(self):
        self.assertEqual(clean_input("  Hello World  "), "hello_world")

    def test_uppercase_conversion(self):
        self.assertEqual(clean_input("PYTHON_IS_COOL"), "python_is_cool")
        self.assertEqual(clean_input("gEmInI"), "gemini")

    def test_multiple_spaces_handling(self):
        self.assertEqual(clean_input("admin    user"), "admin____user")

    def test_leading_trailing_spaces(self):
        self.assertEqual(clean_input("   trim_me"), "trim_me")
        self.assertEqual(clean_input("trim_me   "), "trim_me")

    def test_empty_string(self):
        self.assertEqual(clean_input(""), "")
        self.assertEqual(clean_input("   "), "")

if __name__ == '__main__':
    unittest.main()