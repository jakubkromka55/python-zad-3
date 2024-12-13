# Funkcja obliczająca sumę cyfr w liczbie
def sum_digits(number):
    # Zamiana liczby na jej wartość bezwzględną (dla obsługi liczb ujemnych)
    number = abs(number)
    
    # Konwersja liczby na ciąg znaków, aby przejść po każdej cyfrze
    number_str = str(number)
    
    # Zmienna do przechowywania sumy cyfr
    sum_of_digits = 0
    
    # Iteracja po każdej cyfrze w liczbie
    for digit in number_str:
        sum_of_digits += int(digit)  # Zamiana znaku na liczbę całkowitą i dodanie do sumy
    
    # Zwrócenie wyniku
    return sum_of_digits

# Odczytanie liczby od użytkownika
any_number = int(input('Enter integer number: '))

# Obliczenie sumy cyfr
result = sum_digits(any_number)

# Wypisanie wyniku
print(f'The sum of the digits in the number {any_number} is {result}')
