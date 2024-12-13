def f(n):
    # Generujemy ciąg liczb od 1 do n
    return "".join(str(i) for i in range(1, n + 1))

# Testowanie funkcji
print(f(11))  # Oczekiwany wynik: "1234567891011"
print(f(4))   # Oczekiwany wynik: "1234"
