# Funkcja maskująca numer karty kredytowej
def hide(card_number):
    # Zamienia numer karty na ciąg, w którym tylko pierwsze 2 i ostatnie 4 cyfry są widoczne
    return card_number[:2] + '*' * 10 + card_number[-4:]
