import turtle as t

#Draw 6
while True:
  t.shape("circle")
  t.forward(200)
  t.left(170)
  if abs(t.pos()) < 1:
    t.write((int(t.position()[0]), f"{int(t.position()[1])}i"), font=("Times new roman", 12, "normal"))
    break

t.exitonclick()