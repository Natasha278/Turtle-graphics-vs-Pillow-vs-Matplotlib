import turtle as t

t.bgcolor = 'white'
t.hideturtle  
c = input('Enter the color of the square (White or Black): ').capitalize()
l = 100

position = []

def square(color = 'black'):
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
        if color == 'White':
          square(color)
          t.forward(l)
          square()
          t.forward(l)
        else:
          square()
          t.forward(l)
          square('white')
          t.forward(l)
      t.goto(position[-3])
      for _ in range(4):
        if color == 'White':
          t.backward(l)
          square(color)
          t.backward(l)
          square()
        else:
          t.backward(l)
          square()
          t.backward(l)
          square('white')
      t.goto(position[-2])
      
t.penup()
t.goto(-4*l, -4*l) 
t.pendown()
t.speed(0)
board(c)
t.done()

print(position)
