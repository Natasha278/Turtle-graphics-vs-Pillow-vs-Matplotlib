import turtle as t

c = input('Choose color to play (White or Black): ').capitalize()
t.bgcolor('white')
l = 100
positions = []

def missing(color):
    return 'White' if color == 'Black' else 'Black'

def square(color, direction):
    t.color("black", color)
    t.begin_fill()
    for _ in range(4):  
        t.forward(l)
        getattr(t, direction)(90)
    t.end_fill()

def board(start_color):
    current_color = start_color
    for row in range(8):
        for _ in range(8):
            square(current_color, 'right')
            t.forward(l)
            current_color = missing(current_color)
        t.penup()
        t.goto(-4*l, -3*l + (row + 1) * l)
        t.pendown()
        current_color = missing(current_color)

t.hideturtle()
t.penup()
t.goto(-4*l, -3*l)
t.pendown()
t.speed(0)
board(c)
t.done()