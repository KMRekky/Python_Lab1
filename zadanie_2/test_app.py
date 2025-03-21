import unittest
from app import is_valid_email, calculate_circle_area, filter_even_numbers, convert_date_format, is_palindrome

class TestApp(unittest.TestCase):

    def setUp(self):
        self.valid_email = "valid@example.com"
        self.invalid_email = "invalid-email"
        self.circle_radius = 5
        self.numbers = [1, 2, 3, 4, 5, 6]
        self.date_str = "2023-03-21"
        self.palindrome_text = "A man a plan a canal Panama"
        self.non_palindrome_text = "This is not a palindrome"

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email(self.valid_email))  
        self.assertFalse(is_valid_email(self.invalid_email))  

    def test_calculate_circle_area(self):
        self.assertEqual(calculate_circle_area(self.circle_radius), 78.53981633974483) 
        with self.assertRaises(ValueError):  
            calculate_circle_area(-1)

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers(self.numbers), [2, 4, 6])  
        with self.assertRaises(TypeError):  
            filter_even_numbers("not a list")

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format(self.date_str), "21/03/2023") 
        with self.assertRaises(ValueError):  
            convert_date_format("2023-03-21T12:00:00")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(self.palindrome_text)) 
        self.assertFalse(is_palindrome(self.non_palindrome_text)) 

    def test_is_valid_email_parametrized(self):
        test_cases = [
            ("valid@example.com", True),
            ("invalid-email", False),
            ("@missinguser.com", False),
            ("user@domain", False),
            ("another@valid.com", True)
        ]
        for email, expected in test_cases:
            with self.subTest(email=email):
                self.assertEqual(is_valid_email(email), expected)

    def test_calculate_circle_area_parametrized(self):
        test_cases = [
            (5, 78.53981633974483),
            (10, 314.1592653589793),
            (0, 0),
            (-1, ValueError)
        ]
        for radius, expected in test_cases:
            with self.subTest(radius=radius):
                if expected == ValueError:
                    with self.assertRaises(ValueError):
                        calculate_circle_area(radius)
                else:
                    self.assertEqual(calculate_circle_area(radius), expected)


if __name__ == '__main__':
    unittest.main()
