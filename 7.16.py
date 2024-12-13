def f(n):
    if n == 0:  # Pierwsza wartość ciągu
        return 0
    elif n == 1:  # Druga wartość ciągu
        return 1
    
    # Inicjalizacja dwóch pierwszych wartości ciągu
    a, b = 0, 1
    
    # Iteracyjnie obliczamy kolejne wartości ciągu
    for _ in range(2, n + 1):
        a, b = b, a + b  # Obliczamy kolejną wartość i przesuwamy wskaźniki
    
    return b

# Testowanie funkcji
print(f(5))  # Oczekiwany wynik: 3
print(f(9))  # Oczekiwany wynik: 21
print(f(0))  # Oczekiwany wynik: 0
print(f(1))  # Oczekiwany wynik: 1
print(f(10)) # Oczekiwany wynik: 34
