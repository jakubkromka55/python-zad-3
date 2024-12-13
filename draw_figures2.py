import turtle
from figures2 import draw_square, draw_triangle, draw_rectangle  # Importujemy funkcje

# Ustawienie ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")  # Ustawienie koloru tła ekranu

# Tworzymy żółwia
pen = turtle.Turtle()
pen.speed(5)  # Ustawiamy prędkość rysowania

# Rysowanie figury 1: Kwadrat
pen.penup()  # Podnosimy długopis, aby żółw nie rysował
pen.goto(-100, 100)  # Przesuwamy żółwia do współrzędnych (-100, 100)
pen.pendown()  # Odkładamy długopis, aby zacząć rysować
draw_square(100)  # Rysujemy kwadrat o boku 100

# Rysowanie figury 2: Kwadrat w innym miejscu
pen.penup()
pen.goto(100, -100)
pen.pendown()
draw_square(100)  # Rysujemy kolejny kwadrat

# Rysowanie figury 3: Trójkąt równoramienny
pen.penup()
pen.goto(-200, 0)  # Przesuwamy żółwia w inne miejsce
pen.pendown()
draw_triangle(100)  # Rysujemy trójkąt równoramienny

# Rysowanie figury 4: Trójkąt w innym miejscu
pen.penup()
pen.goto(200, 0)  # Przesuwamy żółwia w inne miejsce
pen.pendown()
draw_triangle(100)  # Rysujemy kolejny trójkąt

# Rysowanie figury 5: Prostokąt
pen.penup()
pen.goto(-200, -200)  # Przesuwamy żółwia w inne miejsce
pen.pendown()
draw_rectangle(150, 100)  # Rysujemy prostokąt

# Rysowanie figury 6: Prostokąt w innym miejscu
pen.penup()
pen.goto(200, -200)  # Przesuwamy żółwia w inne miejsce
pen.pendown()
draw_rectangle(150, 100)  # Rysujemy kolejny prostokąt

# Ukrywamy żółwia po rysowaniu
pen.hideturtle()

# Utrzymanie okna aż do jego zamknięcia
window.mainloop()
