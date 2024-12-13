def f(n):
    # Tworzymy ciąg gwiazdek oddzielonych ukośnikami
    return "/".join(["*"] * n)

# Testowanie funkcji
print(f(4))  # Oczekiwany wynik: "*/*/*/*"
print(f(1))  # Oczekiwany wynik: "*"
print(f(0))  # Oczekiwany wynik: "" (brak gwiazdek)
