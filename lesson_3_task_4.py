import turtle

t = turtle.Turtle()
t.speed(3)  # Средняя скорость рисования

# Голова
t.circle(50)

# Глаза
t.penup()
t.goto(-15, 60)
t.dot(10, "green")
t.goto(15, 60)
t.dot(10, "green")

# Нос
t.goto(0, 50)
t.dot(5, "pink")

# Рот
t.goto(0, 40)
t.setheading(-90)
t.pendown()
t.circle(10, 180)

# Уши
t.penup()
t.goto(-30, 90)
t.pendown()
t.begin_fill()
t.goto(-50, 120)
t.goto(-20, 100)
t.end_fill()

t.penup()
t.goto(30, 90)
t.pendown()
t.begin_fill()
t.goto(50, 120)
t.goto(20, 100)
t.end_fill()

t.hideturtle()
turtle.done()