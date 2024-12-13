def f(number1, number2, number3):
    """Zwraca różnicę między największą i najmniejszą liczbą."""
    max_number = max(number1, number2, number3)
    min_number = min(number1, number2, number3)
    return max_number - min_number

# Testy
print(f(7, 4, 9))  # Oczekiwany wynik: 5
print(f(2, 12, 8))  # Oczekiwany wynik: 10
print(f(-5, -1, -10))  # Oczekiwany wynik: 9
