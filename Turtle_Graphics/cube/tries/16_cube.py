import turtle as t
import time 

t.bgcolor('black')
t.hideturtle()
t.speed(0)

points = [(0, 0)]

def square():
  for _ in range(4):
    t.forward(100)
    t.left(90)
    points.append((int(t.position()[0]), int(t.position()[1])))

def cube():
  t.color('white')
  t.goto(0, 0)
  square()
  t.penup()
  t.goto(points[1])
  t.left(45)
  t.forward(70)
  t.right(45)
  t.backward(100)
  t.pendown()
  square()
  t.penup()
  t.right(135)
  t.pendown()
  t.forward(70)
  t.penup()
  for i in range(4):
    t.goto(points[i])
    t.pendown()
    t.goto(points[i+4])
    t.penup()




cube()
t.done()