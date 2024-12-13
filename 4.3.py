import math

# Funkcja obliczająca pole trójkąta za pomocą wzoru Herona
def triangle_area(a, b, c):
    # Obliczamy półobwód
    s = (a + b + c) / 2
    # Obliczamy pole trójkąta według wzoru Herona
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Odczytanie boków trójkąta od użytkownika
a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

# Obliczanie pola trójkąta
area = triangle_area(a, b, c)

# Wypisanie wyniku
print(f'Pole trójkąta o bokach {a}, {b}, {c} wynosi {area:.2f}')

# Obliczanie pól trójkątów dla podanych wymiarów
print('Pole trójkąta o bokach 3, 4, 5 wynosi', triangle_area(3, 4, 5))
print('Pole trójkąta o bokach 5, 12, 13 wynosi', triangle_area(5, 12, 13))
print('Pole trójkąta o bokach 7, 24, 25 wynosi', triangle_area(7, 24, 25))
