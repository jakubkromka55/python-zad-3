def f(n):
    def is_prime(num):
        """Sprawdza, czy liczba num jest liczbą pierwszą."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0  # Licznik liczb pierwszych
    candidate = 1  # Kandydat na liczbę pierwszą

    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1

    return candidate

# Testy
print(f(1))  # Oczekiwany wynik: 2
print(f(5))  # Oczekiwany wynik: 11























#print(f(10)) # Oczekiwany wynik: 29
