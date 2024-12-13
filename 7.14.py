def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "Invalid operator"

# Testowanie funkcji
print(f(2, 3, "+"))   # Oczekiwany wynik: 5
print(f(2, 3, "%"))   # Oczekiwany wynik: 2
print(f(2, 3, "**"))  # Oczekiwany wynik: 8
print(f(2, 3, "*"))   # Oczekiwany wynik: 6
print(f(2, 3, "-"))   # Oczekiwany wynik: -1
