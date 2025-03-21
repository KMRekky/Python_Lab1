import re
from datetime import datetime

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    return 3.141592653589793 * radius * radius

def filter_even_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Wejście musi być listą")
    return [num for num in numbers if num % 2 == 0]

def convert_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Zły format daty")

def is_palindrome(text):
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    return cleaned_text == cleaned_text[::-1]
