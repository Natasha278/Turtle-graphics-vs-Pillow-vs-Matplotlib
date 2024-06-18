import turtle as t
import time 

t.bgcolor('black')
t.hideturtle()
t.speed(0)

points = [(0, 0)]

def cube():
  t.color('white')
  t.goto(0, 0)
  for i in range(4):
    t.forward(100)
    t.left(90)
    points.append((int(t.position()[0]), int(t.position()[1])))
  t.penup()
  t.goto(points[0])

  t.left(45)
  t.pendown()
  t.forward(70)
  t.right(45)
  t.forward(100)
  points.append((int(t.position()[0]), int(t.position()[1])))
  t.right(45)
  t.right(90)
  t.forward(70)

  t.penup()
  t.goto(points[3])
  t.pendown()
  t.right(180)
  t.forward(70)
  t.right(45)
  t.forward(100)
  t.right(135)
  t.forward(70)
  t.penup()
  t.goto(0,0)
  t.right(45)
  t.backward(100)
  t.right(90)
  t.goto(points[5])
  t.pendown()
  for i in range(4):
    t.forward(100)
    t.left(90)
    points.append((int(t.position()[0]), int(t.position()[1])))


cube()
t.done()