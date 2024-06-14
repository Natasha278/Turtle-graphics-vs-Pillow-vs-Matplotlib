import turtle as t

#Screen characteristics
t.speed(0)
t.title("Mandelbrot Set")
t.setup(800, 800)
t.bgcolor("white")
t.hideturtle()

#variables
MAX_N = 100
WIDTH, HEIGHT = 800, 800
SCALE = 200

#functions
def mandelbrot(c):
    z = 0
    for n in range(MAX_N):
        z = z*z + c
        if abs(z) > 2:
            return n
    return MAX_N

# Mapping screen coordinates to complex plane
def screen_to_complex(x, y):
    return (x - WIDTH // 2) / SCALE, (y - HEIGHT // 2) / SCALE

# Plotting Mandelbrot set
for x in range(-WIDTH // 2, WIDTH // 2):
    for y in range(-HEIGHT // 2, HEIGHT // 2):
        re, im = screen_to_complex(x, y)
        c = complex(re, im)
        m = mandelbrot(c)
        if m == MAX_N:
            t.color("black")
        else:
            t.color((m / MAX_N, m / MAX_N, m / MAX_N))
        t.goto(x, y)
        t.dot(1)

# Keep the window open
t.done()