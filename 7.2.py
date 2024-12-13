# Funkcja dodająca dwie liczby
def add(a, b):
    return a + b

# Funkcja odejmująca dwie liczby
def subtract(a, b):
    return a - b

# Funkcja główna programu, w której umieszczona jest logika działania
def main():

    x = 10
    y = 5
    
    # Wyświetlanie wyników dodawania i odejmowania
    print(f"Dodawanie: {add(x, y)}")      # Wyświetla wynik dodawania
    print(f"Odejmowanie: {subtract(x, y)}")  # Wyświetla wynik odejmowania

# Blok kodu poniżej zostanie wykonany tylko wtedy, gdy plik będzie uruchamiany bezpośrednio
if __name__ == "__main__":
    # Wywołanie funkcji głównej programu
    main()
