import turtle as t

#Draw 4
drawing_area = t.Screen()
t.shape("circle")
t.shapesize(0.1, 0.1, 0.1)
t.forward(200)
t.right(90)
t.forward(10)
t.write((int(t.position()[0]), f"{int(t.position()[1])}i"), font=("Times new roman", 12, "normal"))
t.exitonclick()