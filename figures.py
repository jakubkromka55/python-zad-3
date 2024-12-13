import turtle

# Funkcja rysująca kwadrat o podanej długości boku
def draw_square(length):
    # Tworzymy żółwia
    pen = turtle.Turtle()
    pen.speed(5)  # Ustawiamy prędkość rysowania

    # Rysowanie kwadratu
    for i in range(4):
        pen.forward(length)  # Przesuwamy żółwia do przodu o 'length'
        pen.right(90)  # Obracamy żółwia o 90 stopni w prawo

    # Ukrywamy żółwia po rysowaniu
    pen.hideturtle()
