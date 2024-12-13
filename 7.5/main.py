# Importowanie funkcji is_in_range z modułu range_check
from range_check import is_in_range

# Wprowadzenie liczby przez użytkownika
number = int(input("A number: "))

# Określenie zakresu
x = 2
y = 15

# Sprawdzanie, czy liczba mieści się w określonym zakresie
if is_in_range(number, x, y):
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")
