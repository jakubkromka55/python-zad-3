# Funkcja sprawdzająca, czy liczba mieści się w zakresie <x, y>
def is_in_range(number, x, y):
    # Funkcja zwraca True, jeśli liczba mieści się w zakresie <x, y>, w przeciwnym razie False
    return x < number < y
