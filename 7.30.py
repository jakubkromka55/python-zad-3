def sum_natural(n):
    # Warunek bazowy: suma liczb od 1 do 1 to 1
    if n == 1:
        return 1
    # Rekurencyjne wywołanie: suma od 1 do n to n + suma od 1 do n-1
    else:
        return n + sum_natural(n - 1)

# Obliczamy sumę liczb naturalnych z zakresu <1, 10>
n = 10
result = sum_natural(n)
print(f"Suma liczb naturalnych od 1 do {n} wynosi {result}")
