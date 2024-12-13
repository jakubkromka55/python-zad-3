import turtle

# Ustawienie ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")  # Ustawienie koloru tła ekranu

# Tworzymy żółwia
pen = turtle.Turtle()
pen.speed(5)  # Ustawiamy prędkość rysowania

# Długość boku kwadratu
side_length = 100

# Rysowanie kwadratu
for i in range(4):
    pen.forward(side_length)  # Przesuwamy żółwia do przodu o 'side_length'
    pen.right(90)  # Obracamy żółwia o 90 stopni w prawo

# Ukrywamy żółwia po rysowaniu
pen.hideturtle()

# Utrzymanie okna aż do jego zamknięcia
window.mainloop()
