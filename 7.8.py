# Funkcja obliczająca minimalną liczbę monet
def f(amount_to_pay):
    # Liczba monet
    coins_count = 0

    # Najpierw używamy jak najwięcej monet 5 zł
    coins_count += amount_to_pay // 5
    amount_to_pay %= 5  # Pozostająca kwota po użyciu monet 5 zł

    # Następnie używamy monet 2 zł
    coins_count += amount_to_pay // 2
    amount_to_pay %= 2  # Pozostająca kwota po użyciu monet 2 zł

    # Na końcu używamy monet 1 zł
    coins_count += amount_to_pay // 1
    amount_to_pay %= 1  # Pozostająca kwota (powinna być 0)

    return coins_count

# Testowanie funkcji
print(f(23))  # 6
print(f(8))   # 3
print(f(2))   # 1
print(f(0))   # 0
