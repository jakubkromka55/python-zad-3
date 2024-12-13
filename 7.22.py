def f(name):
    #Zwraca akronim utworzony z pierwszych liter każdego słowa.
    words = name.split()  # Dzieli tekst na słowa
    acronym = ''.join(word[0].upper() for word in words)  # Pobiera pierwsze litery i łączy w akronim
    return acronym

# Testy
print(f("Internet of Things"))  # Oczekiwany wynik: IoT
print(f("For Your Information"))  # Oczekiwany wynik: FYI
print(f("Python"))  # Oczekiwany wynik: P
