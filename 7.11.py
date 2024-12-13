def f(n1, n2, n3):
    # Sprawdzamy, czy przynajmniej jedna z liczb jest ujemna
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else:
        return False

# Testowanie funkcji
print(f(11, 6, -4))  # Oczekiwany wynik: True (bo -4 jest liczbą ujemną)
print(f(5, 4, 14))    # Oczekiwany wynik: False (wszystkie liczby są dodatnie)
print(f(-1, 2, 3))    # Oczekiwany wynik: True (bo -1 jest liczbą ujemną)
print(f(0, 0, 0))     # Oczekiwany wynik: False (wszystkie liczby są 0)
