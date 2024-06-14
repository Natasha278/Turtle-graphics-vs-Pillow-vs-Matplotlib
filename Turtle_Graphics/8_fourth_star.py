import turtle as t

t.shape("circle")
t.color("red", "yellow")
t.speed(100)
#size of the line 
t.pensize(5)
t.begin_fill()

def write_pos():
    pos_text = f"({int(t.position()[0])}, {int(t.position()[1])}i)"
    t.write(pos_text, font=("Times New Roman", 12, "normal"))

for i in range(20):
    t.forward(200)
    t.left(170)
    write_pos()
t.exitonclick()
t.end_fill()
