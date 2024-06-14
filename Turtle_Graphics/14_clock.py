import turtle as t
import time

#Draw 14
t.hideturtle()
t.speed(100)

def outer_circle():
    t.color('black', 'black')
    t.begin_fill()
    t.circle(105)
    t.end_fill()

def inner_circle():
    t.color('black', 'white')
    t.begin_fill()
    t.circle(75)
    t.end_fill()

def write_hours():
    t.left(25)
    t.color('red')
    for i in range(1, 13):
        t.penup()
        t.forward(180)
        t.right(15)
        t.pendown()
        t.write(str(i), font=("Times new roman", 12, "normal"))
        t.penup()
        t.backward(180)
        t.right(15)
        t.pendown()

# def hands():
#     t.color('red')
#     t.pensize(2)
#     angle_seconds = 360/60
#     angle_hours = 360/12
#     t.goto(0, 100)
#     t.left(20)
#     t.pendown()
#     t.forward(60)
#     seconds = 0
#     #seconds < 61
#     while seconds < 60:
#         #t.speed(0)
#         seconds += 1
#         t.undo()
#         t.right(angle_seconds)
#         t.forward(60)
#         # if seconds == 60:
#         #     t.right(6)
#         #     t.forward(60)
#         #     t.undo()
#         #     t.goto(0, 100)
#         #     t.left(20)
#         #     seconds = 0
#     for i in range(60):
#         pass
#         # time.sleep(1)
#         # t.undo()
#         # t.right(angle)
#         # t.forward(60)
def second_hand():
    t.color('red')
    t.pensize(2)
    t.speed(0)
    angle_seconds = 360 / 60
    t.penup()
    t.setheading(90)  # Apunta la aguja hacia arriba, 90 grados
    t.pendown()
    while True:
        start_time = time.time()
        for _ in range(60):
            elapsed_time = time.time() - start_time
            if elapsed_time >= 1:
                break
            t.undo()
            t.penup()
            t.goto(0, 100)
            t.pendown()
            t.setheading(90 - (elapsed_time * angle_seconds * 60)) 
            t.forward(60)
            time.sleep(0.01)

def minute_hand():
    t.color('red')
    t.pensize(4)
    t.speed(0)
    angle_seconds = 360 / 60
    t.penup()
    t.setheading(90)
    t.pendown()
    while True:
        start_time = time.time()
        for _ in range(60):
            elapsed_time = time.time() - start_time
            if elapsed_time >= 1:
                break
            t.undo()
            t.penup()
            t.goto(0, 100)
            t.pendown()
            t.setheading(90 - (elapsed_time * angle_seconds * 60)) 
            t.forward(60)
            time.sleep(0.01)
        

outer_circle()
t.penup()
t.goto(0, 30)
t.pendown()
inner_circle()
t.penup()
t.goto(-25, 10)
t.pendown()
t.left(45)
write_hours()
t.penup()
second_hand()

t.exitonclick()