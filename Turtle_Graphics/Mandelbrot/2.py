# import turtle as t

# #Screen characteristics
# t.speed(0)
# t.title("Mandelbrot Set")
# t.setup(800, 800)
# t.bgcolor("white")
# t.hideturtle()

# #variables
# MAX_N = 100

# #functions
# c = x + i*y
# c_square = x**2 - y**2 + 2*x*y*i

# def z(x, y, n):
#   if n == 0:
#     return (0, 0);

#   val = z(x, y, n - 1)

#   return (val[0] ** 2 - val[1] ** 2 + x, 2 * val[0] * val[1] + y)
  

# def sale(x, y):
#   if z(x, y, MAX_N) > 2:
#     return True
#   else:
#     return False


# for x in range(0, MAX_X):
#   for y in range(0, MAX_Y):
#     if sale(x, y):
#       t.goto(x, y)
#       t.shape("circle")
#       t.color("white")
#     else:
#       t.goto(x, y)
#       t.shape("circle")
#       t.color("black")