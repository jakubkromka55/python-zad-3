def f(password):
    #Sprawdza, czy hasło jest poprawne: ma co najmniej 6 znaków i brak powtórzeń.
    # Sprawdzenie długości hasła
    if len(password) < 6:
        return False
    
    # Sprawdzenie, czy hasło zawiera powtarzające się znaki
    if len(password) != len(set(password)):  # Porównujemy długość hasła z długością zbioru unikalnych znaków
        return False
    
    return True

# Testy
print(f("ax15"))       # Oczekiwany wynik: False (za krótkie)
print(f("book123"))     # Oczekiwany wynik: False (powtórzenie "o")
print(f("A2water3"))    # Oczekiwany wynik: True (poprawne hasło)
print(f("qwerty"))      # Oczekiwany wynik: True (poprawne hasło)
print(f(""))            # Oczekiwany wynik: False (puste hasło)
