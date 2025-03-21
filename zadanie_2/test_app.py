import unittest
from app import is_valid_email, calculate_circle_area, filter_even_numbers, convert_date_format, is_palindrome

class TestApp(unittest.TestCase):

    def setUp(self):
        """Inicjalizacja danych wejściowych używanych w testach"""
        self.valid_email = "valid@example.com"
        self.invalid_email = "invalid-email"
        self.circle_radius = 5
        self.numbers = [1, 2, 3, 4, 5, 6]
        self.date_str = "2023-03-21"
        self.palindrome_text = "A man a plan a canal Panama"
        self.non_palindrome_text = "This is not a palindrome"

    def test_is_valid_email(self):
        """Test sprawdzający poprawność adresu e-mail"""
        self.assertTrue(is_valid_email(self.valid_email))  # Poprawny email
        self.assertFalse(is_valid_email(self.invalid_email))  # Niepoprawny email

    def test_calculate_circle_area(self):
        """Test obliczania pola koła"""
        self.assertEqual(calculate_circle_area(self.circle_radius), 78.53981633974483)  # Oczekiwane pole koła
        with self.assertRaises(ValueError):  # Sprawdzamy, czy wyjątek jest zgłaszany dla ujemnego promienia
            calculate_circle_area(-1)

    def test_filter_even_numbers(self):
        """Test filtracji liczb parzystych"""
        self.assertEqual(filter_even_numbers(self.numbers), [2, 4, 6])  # Sprawdzamy, czy zwrócone zostaną liczby parzyste
        with self.assertRaises(TypeError):  # Sprawdzamy, czy błąd jest zgłaszany, gdy wejście nie jest listą
            filter_even_numbers("not a list")

    def test_convert_date_format(self):
        """Test konwersji formatu daty"""
        self.assertEqual(convert_date_format(self.date_str), "21/03/2023")  # Sprawdzamy poprawność konwersji
        with self.assertRaises(ValueError):  # Sprawdzamy, czy błąd jest zgłaszany dla nieprawidłowego formatu daty
            convert_date_format("2023-03-21T12:00:00")

    def test_is_palindrome(self):
        """Test sprawdzający, czy tekst jest palindromem"""
        self.assertTrue(is_palindrome(self.palindrome_text))  # Sprawdzamy, czy tekst jest palindromem
        self.assertFalse(is_palindrome(self.non_palindrome_text))  # Sprawdzamy, że tekst nie jest palindromem

    def test_is_valid_email_parametrized(self):
        """Testy parametryzowane dla sprawdzenia adresów e-mail"""
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
        """Testy parametryzowane dla obliczania pola koła"""
        test_cases = [
            (5, 78.53981633974483),
            (10, 314.1592653589793),
            (0, 0),
            (-1, ValueError)  # Oczekujemy błędu dla ujemnego promienia
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
