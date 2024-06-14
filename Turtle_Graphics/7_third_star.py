import turtle as t

#Draw 7
t.shape("circle")
t.speed(100) 
def write_pos():
    pos_text = f"({int(t.position()[0])}, {int(t.position()[1])}i)"
    t.write(pos_text, font=("Times new roman", 12, "normal"))

def move_turtle():
    global timer_id
    t.forward(200)
    t.left(170)
    write_pos()
    timer_id = t.ontimer(lambda: t.undo(), 1000)
    if abs(t.pos()) < 1:
        write_pos()
    else:
        t.ontimer(move_turtle, 1000)  
move_turtle()
t.exitonclick()
