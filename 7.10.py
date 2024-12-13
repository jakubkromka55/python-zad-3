def f(x, y):
    count = 0
    # Iterujemy po liczbach w zakresie <x, y>
    for i in range(x, y + 1):
        if i < 0 and i % 2 == 0:  # Sprawdzamy, czy liczba jest ujemna i parzysta
            count += 1
    return count

# Testowanie funkcji
print(f(-7, 8))  # Oczekiwany wynik: 3 (liczby: -6, -4, -2)
print(f(-1, 11))  # Oczekiwany wynik: 0 (brak liczb ujemnych parzystych)
print(f(-10, -1))  # Oczekiwany wynik: 5 (liczby: -10, -8, -6, -4, -2)
print(f(0, 20))  # Oczekiwany wynik: 0 (brak liczb ujemnych parzystych)
