# Importowanie funkcji count_letter z modułu letter_count
from letter_count import count_letter

# Tekst, w którym będziemy liczyć literę
text = "You never get a second chance to make a first impression"

# Litera, którą będziemy liczyć
letter = 'e'

# Wywołanie funkcji count_letter i obliczenie liczby wystąpień
letter_count = count_letter(text, letter)

# Wydrukowanie wyniku
print(f"The number of letter '{letter}': {letter_count}")
