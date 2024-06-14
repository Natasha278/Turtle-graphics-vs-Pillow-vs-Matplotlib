import turtle as t

#Draw 13
t.bgcolor("black")
t.pencolor("green")
t.speed(100)
a = 0
b = 0
c = 1

while True:
  t.forward(a)
  t.right(b)
  t.pensize(c)
  a += 3
  b+=1
  c+=0.01
  if b == 210:
    break

t.done()