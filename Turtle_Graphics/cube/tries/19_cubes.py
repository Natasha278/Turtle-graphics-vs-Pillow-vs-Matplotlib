import turtle as t

t.bgcolor('black')
t.hideturtle()
t.speed(0)

def square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    square_points = []
    for _ in range(4):
        t.forward(100)
        t.left(90)
        square_points.append(t.position())
    return square_points

def cube(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('white')
    points = square(x, y)
    
    # Move to the start of the second square
    t.penup()
    t.goto(points[0])
    t.left(45)
    t.forward(70)
    t.right(45)
    second_square_start = t.position()
    second_square_points = square(second_square_start[0], second_square_start[1])
    
    # Connect corresponding corners
    for i in range(4):
        t.penup()
        t.goto(points[i])
        t.pendown()
        t.goto(second_square_points[i])

# Draw positions of cubes
positions = []
t.penup()
t.goto(-300, 0)  # Starting position for the row of cubes
for i in range(4):
    positions.append(t.position())
    t.forward(100)  # Adjusted to avoid overlap

# Draw cubes
for pos in positions:
    cube(pos[0], pos[1])

t.done()
