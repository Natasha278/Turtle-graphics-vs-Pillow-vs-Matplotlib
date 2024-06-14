import turtle as t

#Draw 12
t.bgcolor("black")
t.pencolor("green")
t.speed(100)
a = 0
b = 0

while True:
  t.forward(a)
  t.right(b)
  a += 3
  b+=1
  if b == 210:
    break

t.done()