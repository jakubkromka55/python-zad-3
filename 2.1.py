# Program for testing built-in functions

# Obliczanie i drukowanie największej liczby
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7, 5, 6, 3, 8, 2 is', max_number)

# Obliczanie i drukowanie najmniejszej liczby
min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4, 7, 2, 3, 9, 8 is', min_number)

# Obliczanie długości frazy
str_length = len("informatyka")
print('The number of characters in "informatyka" is', str_length)

# Odczyt listy z klawiatury
user_list = input('Enter a list of numbers separated by spaces: ')
user_list = list(map(int, user_list.split()))
print('The list you entered is:', user_list)

# Konwersja ciągu znaków na liczbę
string_number = "20303"
converted_number = int(string_number)
print(f'The number representing the string "{string_number}" is', converted_number)

# Konwersja liczby dziesiętnej na ciąg binarny
decimal_number = 304
binary_string = bin(decimal_number)
print(f'The binary string representing the decimal number {decimal_number} is', binary_string)

# Konwersja liczby dziesiętnej na ciąg szesnastkowy
hexadecimal_string = hex(decimal_number)
print(f'The hexadecimal string representing the decimal number {decimal_number} is', hexadecimal_string)

# Kod Unicode dla znaku €
unicode_char = '€'
unicode_code = ord(unicode_char)
print(f'The Unicode code point for the character "{unicode_char}" is', unicode_code)

# Wartość bezwzględna liczby
negative_number = -17
absolute_value = abs(negative_number)
print(f'The absolute value of {negative_number} is', absolute_value)
