import turtle as t

#Draw 5
while True:
  t.shape("circle")
  t.forward(200)
  t.left(170)
  t.write((int(t.position()[0]), f"{int(t.position()[1])}i"), font=("Times new roman", 12, "normal"))
  if abs(t.pos()) < 1:
    break

t.exitonclick()