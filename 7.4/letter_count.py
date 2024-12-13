# Funkcja do liczenia wystąpień danej litery w tekście
def count_letter(text, letter):
    # Zliczamy wystąpienia litery w tekście, ignorując wielkość liter
    return text.lower().count(letter.lower())  # Używamy .lower() do ignorowania wielkości liter
