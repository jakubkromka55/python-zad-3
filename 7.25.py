def f(x, y):
    suma = 0
    for i in range(x, y + 1):  # Przechodzimy po liczbach od x do y włącznie
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:  # Sprawdzamy warunki
            suma += i  # Dodajemy liczbę do sumy
    return suma

# Testy
print(f(1, 20))  # Oczekiwany wynik: 24
print(f(10, 30)) # Oczekiwany wynik: 48
