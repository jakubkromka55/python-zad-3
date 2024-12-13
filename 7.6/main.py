# Importowanie funkcji hide z modułu card_utils
from card_utils import hide

# Wprowadzenie numeru karty kredytowej
card_number = input("Enter your credit card number: ")

# Maskowanie numeru karty
masked_card = hide(card_number)

# Drukowanie zamaskowanego numeru karty
print("Masked card number:", masked_card)
