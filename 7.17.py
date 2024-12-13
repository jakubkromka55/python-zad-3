def f(palindrome):
    # Zamieniamy ciąg na małe litery, aby ignorować wielkość liter
    palindrome = palindrome.lower()
    
    # Sprawdzamy, czy ciąg jest taki sam od przodu i od tyłu
    return palindrome == palindrome[::-1]

# Testowanie funkcji
print(f("radar"))          # Oczekiwany wynik: True
print(f("12-11-21"))       # Oczekiwany wynik: True
print(f("book"))           # Oczekiwany wynik: False
