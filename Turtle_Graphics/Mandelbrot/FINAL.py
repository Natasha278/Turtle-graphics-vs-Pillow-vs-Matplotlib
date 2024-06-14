import turtle as t

screen = t.Screen()
screen.setup(width=1000, height=600)
screen.title("Mandelbrot Set")
screen.bgcolor("white")
t.speed(0)
t.hideturtle()

# Number of iterations 
max_iter = 100

# Function to check if the complex number c is in the set
def is_in_set(c):
    z = 0 + 0j
    for _ in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return False
    return True

# Drawing Mandelbrot set
step = 2
for x in range(-500, 500):
    for y in range(-300, 300):
        # Adjust x and y to correspond to the complex plane coordinates
        re = (x / 250) * 4 - 2
        im = (y / 150) * 2 - 1
        c = complex(re, im)
        if is_in_set(c):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(2, "black")  # Increase dot size for visibility
    
    # Periodically update the screen to reflect the progress
    # if x % 50 == 0:
    #     screen.update()

# Final screen update
# screen.update()

# Keep the window open until closed by the user
screen.mainloop()
