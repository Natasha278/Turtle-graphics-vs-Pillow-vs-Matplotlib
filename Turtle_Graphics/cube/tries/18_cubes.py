import turtle as t

t.bgcolor('black')
t.hideturtle()
t.speed(0)

# draw many cubes in a row
points = []

def square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.left(90)
        points.append((int(t.position()[0]), int(t.position()[1])))

def cube(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('white')
    square(x, y)
    t.penup()
    t.goto(x, y)
    t.left(45)
    t.forward(70)
    t.right(45)
    t.pendown()
    square(int(t.position()[0]), int(t.position()[1]))
    t.penup()
    for i in range(4):
        t.goto(points[i])
        t.pendown()
        t.goto(points[i+4])
        t.penup()

# draw positions of cubes
position = []
t.goto(-300, 0)
for i in range(4):
    t.penup()
    t.forward(150)  # Adjusted to avoid overlap
    position.append((t.position()[0], t.position()[1]))

# draw cubes
for i in range(len(position)):
    cube(position[i][0], position[i][1])

t.done()
