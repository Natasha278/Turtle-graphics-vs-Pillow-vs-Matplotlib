import turtle as t
import time 

t.bgcolor('black')
# t.hideturtle()
t.speed(0)

# points = []
position = [(-300, 0), (-100, 0), (100, 0)]
points = []
full = 0


def square(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  for _ in range(4):
    t.forward(100)
    t.left(90)
    points.append((int(t.position()[0]), int(t.position()[1])))

for i in range(len(position)):
    x, y = position[i]
    t.color('white')
    square(x, y)
    t.forward(100)

mod_points = points[0:9:4]

print(mod_points)
for j in range(len(mod_points)):
  a, b = mod_points[j]
  t.penup()
  t.goto(a, b)
  t.left(45)
  t.forward(70)
  t.right(45)
  t.backward(100)
  t.pendown()
  square(t.position()[0], t.position()[1])
  t.penup()
  t.right(135)
  t.pendown()
  t.forward(70)
  t.left(135)
  t.penup()
  t.goto(a, b)
  t.pendown()
  t.goto(a + 50, b + 50) 
  t.penup()
  t.goto(a, b + 100)
  t.pendown()
  t.goto(a + 50, b + 150)
  t.penup()
  t.goto(a - 100, b + 100)
  t.pendown()
  t.goto(a - 50, b + 150)

print(points)
t.done()