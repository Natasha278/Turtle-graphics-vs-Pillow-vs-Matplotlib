import turtle as t

#Draw 9
t.shape("turtle")
t.speed(100)
drawing_area = t.Screen()
t.color("red", "blue")
t.pensize(5)
t.begin_fill()
for i in range(36):
    t.forward(500)
    t.left(170) 
t.end_fill()
t.exitonclick()