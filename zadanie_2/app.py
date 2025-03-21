import re
from datetime import datetime

# Funkcja sprawdzająca poprawność adresu e-mail
def is_valid_email(email):
    """Sprawdza, czy adres e-mail jest poprawny"""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

# Funkcja obliczająca pole koła
def calculate_circle_area(radius):
    """Oblicza pole koła o zadanym promieniu"""
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    return 3.141592653589793 * radius * radius

# Funkcja filtrująca liczb parzystych z listy
def filter_even_numbers(numbers):
    """Filtruje liczby parzyste z listy"""
    if not isinstance(numbers, list):
        raise TypeError("Wejście musi być listą")
    return [num for num in numbers if num % 2 == 0]

# Funkcja konwertująca format daty z 'YYYY-MM-DD' na 'DD/MM/YYYY'
def convert_date_format(date_str):
    """Konwertuje datę z formatu 'YYYY-MM-DD' na 'DD/MM/YYYY'"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Zły format daty")

# Funkcja sprawdzająca, czy tekst jest palindromem
def is_palindrome(text):
    """Sprawdza, czy dany tekst jest palindromem"""
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    return cleaned_text == cleaned_text[::-1]
