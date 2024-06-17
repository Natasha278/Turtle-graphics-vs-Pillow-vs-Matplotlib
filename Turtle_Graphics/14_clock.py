import turtle as t
import time

# Initialize turtle
t.hideturtle()
t.speed(0)

# Draw the outer circle
def outer_circle():
    t.penup()
    t.goto(0, -105)
    t.pendown()
    t.color('black', 'black')
    t.begin_fill()
    t.circle(105)
    t.end_fill()

# Draw the inner circle
def inner_circle():
    t.penup()
    t.goto(0, -75)
    t.pendown()
    t.color('black', 'white')
    t.begin_fill()
    t.circle(75)
    t.end_fill()

# Write the hour numbers
def write_hours():
    t.penup()
    t.goto(0, 0)
    t.setheading(60)
    t.color('red')
    for i in range(1, 13):
        t.penup()
        t.forward(90)
        t.pendown()
        t.write(str(i), align="center", font=("Times New Roman", 12, "normal"))
        t.penup()
        t.goto(0, 0)
        t.right(30)

# Draw a clock hand
def draw_hand(angle, length, color, pensize):
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(angle)
    t.pendown()
    t.color(color)
    t.pensize(pensize)
    t.forward(length)

# Draw the clock face once
t.tracer(0)
outer_circle()
inner_circle()
write_hours()
t.tracer(1)

# Function to update the clock hands
def update_hands():
    current_time = time.localtime()
    second_angle = current_time.tm_sec * 6
    minute_angle = current_time.tm_min * 6 + current_time.tm_sec * 0.1
    hour_angle = (current_time.tm_hour % 12) * 30 + current_time.tm_min * 0.5

    # Clear only the hands by moving them back to the origin
    t.undo()
    t.undo()
    t.undo()
    
    # Draw the hands
    draw_hand(hour_angle, 50, 'black', 6)
    draw_hand(minute_angle, 70, 'blue', 4)
    draw_hand(second_angle, 90, 'red', 2)

# Main loop to update the hands
while True:
    update_hands()
    time.sleep(1)
