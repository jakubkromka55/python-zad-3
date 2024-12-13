def f(expression):
    #Oblicza wartość wyrażenia matematycznego zawierającego dodawanie i odejmowanie
    try:
        # Używamy eval, aby obliczyć wynik wyrażenia
        return eval(expression)
    except:
        # Jeśli wyrażenie jest niepoprawne, zwracamy None lub inny komunikat
        return "Błędne wyrażenie"

# Testy
print(f("2+3"))       # Oczekiwany wynik: 5
print(f("3+8+1"))     # Oczekiwany wynik: 12
print(f("2+3-4+5-0")) # Oczekiwany wynik: 6
