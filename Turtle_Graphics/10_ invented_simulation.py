import turtle as t

#Draw 10
t.bgcolor("black")
t.hideturtle()
#t.speed(500)
drawing_area = t.Screen()
t.color("red")
t.pensize(0.1)
init = 1
increase = init + 1

for j in range(100):
    init = init + increase
    t.left(10)
    for i in range(4):
        t.forward(init)
        t.left(90)
t.exitonclick()