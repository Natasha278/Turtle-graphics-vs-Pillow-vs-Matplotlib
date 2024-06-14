import turtle as t

#Draw 1
t.hideturtle()
while True:
  t.forward(500)
  t.left(170)
  if abs(t.pos()) < 1:
    break