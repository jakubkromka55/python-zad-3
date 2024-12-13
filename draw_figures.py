import turtle
from figures import draw_square  # Importowanie funkcji rysującej kwadrat z pliku figures.py

# Ustawienie ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")  # Ustawienie koloru tła ekranu

# Długość boku kwadratu
side_length = 100

# Rysowanie kwadratu przy użyciu funkcji z pliku figures.py
draw_square(side_length)

# Utrzymanie okna aż do jego zamknięcia
window.mainloop()
