import turtle as t

t.bgcolor('black') 
t.hideturtle()
t.speed(0)

n = 15
angle = 360/n

def flower():
  t.color('white')
  for _ in range(n):
    for _ in range(100):
      t.left(360/100)
      for _ in range(4):
        t.forward(90)
        t.left(90)
    t.forward(50)
    t.right(angle)

flower()
t.done()