def f(product_code):
    # Sprawdzenie, czy kod ma dokładnie 4 cyfry
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    
    # Pierwsze trzy cyfry kodu
    first_three_digits = product_code[:3]
    
    # Czwórka kontrolna (ostatnia cyfra)
    control_digit = int(product_code[3])
    
    # Obliczenie sumy pierwszych trzech cyfr
    sum_digits = sum(int(digit) for digit in first_three_digits)
    
    # Obliczenie reszty z dzielenia sumy przez 7
    remainder = sum_digits % 7
    
    # Sprawdzamy, czy reszta jest równa czwartej cyfrze
    return remainder == control_digit

# Testy
print(f("1082"))  # True
print(f("2035"))  # True
print(f("1114"))  # False
print(f("7071"))  # False
