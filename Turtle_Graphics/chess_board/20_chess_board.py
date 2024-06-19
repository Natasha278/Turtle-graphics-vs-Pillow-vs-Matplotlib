import turtle as t

t.bgcolor = 'white' 
c = input('Enter the color of the square (White or Black): ').capitalize()
l = 100
position = []

def missing(color):
    if color == 'Black':
        return 'White'
    return 'Black'

def square(color):
  t.color("black", color)
  t.begin_fill()
  for _ in range(4):  
    t.forward(l)
    t.left(90)
    position.append(t.position())
  t.end_fill()

def board(color):
  for _ in range(4):
      for _ in range(4):
        square(color)
        t.forward(l)
        square(missing(color))
        t.forward(l)
      t.goto(position[-3])
      for _ in range(4):
          t.backward(l)
          square(color)
          t.backward(l)
          square(missing(color))
      t.goto(position[-2])

t.hideturtle() 
t.penup()
t.goto(-4*l, -4*l) 
t.pendown()
t.speed(0)
board(c)
t.done()
