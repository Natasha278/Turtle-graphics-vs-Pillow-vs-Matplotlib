import turtle as t

t.bgcolor = 'white'
t.hideturtle  
c = input('Enter the color of the square (White or Black): ').capitalize()

drawing_area = t.Screen()

def square(color = 'black'):
  t.color("black", color)
  t.begin_fill()
  for _ in range(4):  
    t.forward(100)
    t.left(90)
  t.end_fill()

def board(color):
  for _ in range(4):
      for _ in range(4):
        if color == 'White':
          square(color)
          t.forward(100)
          square()
          t.forward(100)
        else:
          square()
          t.forward(100)
          square('white')
          t.forward(100)
      t.left(90)
      t.penup()
      t.forward(100)
      t.right(90)
      t.pendown()
      for _ in range(4):
        if color == 'White':
          t.backward(100)
          square(color)
          t.backward(100)
          square()
        else:
          t.backward(100)
          square()
          t.backward(100)
          square('white')
      t.penup()
      t.left(90)
      t.forward(100)
      t.right(90)
      t.pendown()
      
t.penup()
t.goto(-400, -400) 
t.pendown()
t.speed(0)
board(c)
t.done()


