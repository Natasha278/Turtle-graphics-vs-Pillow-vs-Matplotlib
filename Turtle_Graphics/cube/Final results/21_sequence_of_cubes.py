import turtle as t
import math as m

t.bgcolor('black')
t.hideturtle()
t.speed(0)
angle = 45

position = [(-300, -200), (-300, 100), (-100, -200), (-100, 100), (100, -200), (100, 100)]
points = []

def create_square(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  for _ in range(4):
    t.forward(100)
    t.left(90)
    points.append((int(t.position()[0]), int(t.position()[1])))

def first_square():
  for i in range(len(position)):
      x, y = position[i]
      t.color('white')
      create_square(x, y)
      t.forward(100)

first_square()
mod_points_0 = points[0:len(points):4]
mod_points_1 = points[3:len(points):4]

def second_square():
  for j in range(len(mod_points_0)):
    a, b = mod_points_0[j]
    t.penup()
    t.goto(a + 70*m.cos(angle), b + 70*m.sin(angle))
    t.backward(100)
    t.pendown()
    create_square(t.position()[0], t.position()[1])

second_square()
mod_points_3 = points[round(len(points)/2):len(points)]
mod_points_4 = points[:round(len(points)/2)]

def unify_squares():
  for i in range(24):
    t.penup()
    t.goto(mod_points_3[i])
    t.pendown()
    t.goto(mod_points_4[i])

unify_squares()
t.done()