def f(number):
    digits = str(number)  # Zamiana liczby na ciąg znaków
    seen = {}  # Słownik do zliczania wystąpień cyfr

    # Zliczanie wystąpień cyfr
    for digit in digits:
        if digit in seen:
            seen[digit] += 1
        else:
            seen[digit] = 1

    # Obliczenie sumy powtarzających się cyfr
    total = sum(int(digit) * count for digit, count in seen.items() if count > 1)
    return total

# Testy
print(f(1027))         # Oczekiwany wynik: 0
print(f(230335))       # Oczekiwany wynik: 9
print(f(513553007))    # Oczekiwany wynik: 21
