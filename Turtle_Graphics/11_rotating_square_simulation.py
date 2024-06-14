import turtle as t

#Draw 11
t.hideturtle()
t.speed(100)
t.bgcolor("black")
#t.color("red")
colors = ["red", "dark red"]
for number in range(400):
  t.forward(number + 1)
  t.right(89)
  t.pencolor(colors[number % 2])
t.done()