def power(x, n):
    # Warunek bazowy: x^0 = 1
    if n == 0:
        return 1
    # Rekurencyjne wywołanie: x^n = x * x^(n-1)
    else:
        return x * power(x, n - 1)

# Obliczamy 5^3
result = power(5, 3)
print(f"5^3 = {result}")
