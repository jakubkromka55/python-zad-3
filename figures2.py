import turtle

# Funkcja rysująca kwadrat
def draw_square(length):
    pen = turtle.Turtle()
    pen.speed(5)  # Ustawiamy prędkość rysowania
    for i in range(4):
        pen.forward(length)  # Przesuwamy żółwia do przodu o 'length'
        pen.right(90)  # Obracamy żółwia o 90 stopni w prawo
    pen.hideturtle()  # Ukrywamy żółwia po rysowaniu

# Funkcja rysująca trójkąt równoramienny
def draw_triangle(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for i in range(2):  # Dwa boki trójkąta
        pen.forward(length)  # Rysujemy jeden bok
        pen.left(120)  # Obracamy o 120 stopni (kąt w trójkącie równoramiennym)
    pen.forward(length)  # Rysujemy trzeci bok
    pen.hideturtle()  # Ukrywamy żółwia po rysowaniu

# Funkcja rysująca prostokąt
def draw_rectangle(length_a, length_b):
    pen = turtle.Turtle()
    pen.speed(5)
    for i in range(2):
        pen.forward(length_a)  # Rysujemy jeden bok
        pen.left(90)
        pen.forward(length_b)  # Rysujemy drugi bok
        pen.left(90)
    pen.hideturtle()  # Ukrywamy żółwia po rysowaniu
