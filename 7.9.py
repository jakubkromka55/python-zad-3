def f(number, even):
    # Przekształcamy liczbę na ciąg znaków, aby móc iterować po każdej cyfrze
    number_str = str(number)
    sum_digits = 0
    
    # Iterujemy po każdej cyfrze w liczbie
    for digit in number_str:
        # Zamieniamy cyfrę na liczbę
        digit_int = int(digit)
        
        # Sprawdzamy, czy cyfra jest parzysta czy nieparzysta
        if even:
            # Jeśli 'even' jest True, bierzemy tylko cyfry parzyste
            if digit_int % 2 == 0:
                sum_digits += digit_int
        else:
            # Jeśli 'even' jest False, bierzemy tylko cyfry nieparzyste
            if digit_int % 2 != 0:
                sum_digits += digit_int
                
    return sum_digits

# Testowanie funkcji
print(f(3124, True))  # 6 (cyfry parzyste: 2, 4 -> 2 + 4 = 6)
print(f(3124, False))  # 4 (cyfry nieparzyste: 3, 1 -> 3 + 1 = 4)
print(f(20576, False))  # 12 (cyfry nieparzyste: 5, 7 -> 5 + 7 = 12)
print(f(20576, True))  # 8 (cyfry parzyste: 2, 6 -> 2 + 6 = 8)
print(f(13115, True))  # 0 (brak cyfr parzystych)
