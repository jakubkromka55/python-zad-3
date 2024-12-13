# Funkcja sprawdzająca, czy ciąg jest liczbą binarną
def f(binary_number):
    # Sprawdzenie, czy ciąg zawiera tylko '0' i '1'
    for char in binary_number:
        if char not in '01':  # Jeśli znak nie jest '0' lub '1', zwróć False
            return False
    return True  # Jeśli wszystkie znaki są '0' lub '1', zwróć True

# Testowanie funkcji
print(f("101101"))       # True
print(f("1311a10100"))   # False
