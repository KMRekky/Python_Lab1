# Import modułu math do obliczeń matematycznych
# Dokumentacja: https://docs.python.org/3/library/math.html

import math
list_a = [2, 0, 6, 5, 26]
list_b = [0, 20, 8, 12, 1]

# Łączenie list za pomocą funkcji zip()
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip

zlaczone = list(zip(list_a, list_b))
print('Połączone listy: ', zlaczone)

# Użucie funkcji sqrt() do obliczenia pierwiasta kwadratowego 
liczba = 36
print(f'Pierwiastek kwadratowy z {liczba} = {math.sqrt(liczba)}')

# Wyjątek ValueError
# Dokumentacja: https://docs.python.org/3/library/exceptions.html#ValueError

try:
    a = int(input("Podaj liczbę: "))
    print(f"Pierwiastek z {a}: {math.sqrt(a)}")
except ValueError:
    print("Błąd: Podano nieprawidłową wartość. Wprowadź liczbę całkowitą.")