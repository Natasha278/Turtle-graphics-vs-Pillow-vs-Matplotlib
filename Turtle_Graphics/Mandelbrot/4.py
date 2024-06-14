import turtle as t

#Screen characteristics
t.speed(0)
t.title("Mandelbrot Set")
Max_x, Max_y = 800, 800
t.setup(Max_x, Max_y)
t.bgcolor("white")
t.hideturtle()

#variables
MAX_N = 100

#functions
#Define c as a complex number
def c(x, y):
  return x + y

#Define the square of c to operate with it later 
def c_square(x, y):
  return x**2 - y**2 + 2*x*y

#Define z to return the point once we check if c is in mandelbrot set
#define the recursive function as n
def z(x, y, n):
  #z_0 = 0 C
  if n == 0:
    return (0, 0);
  # z_n = z_(n-1)**2 + c
  val = z(x, y, n - 1)
  return (val[0] ** 2 - val[1] ** 2 + x, 2 * val[0] * val[1] + y)
  
#check if c is in the mandelbrot set z
#we define n as MAX_n to determine the max number of points
def sale(x, y):
  if z(x, y, MAX_N) > 2:
    return True
  else:
    return False

#go throught pixels to paint them 
for x in range(0, Max_x):
  for y in range(0, Max_y):
    if sale(x, y):
      t.goto(x, y)
      t.shape("circle")
      t.color("white")
    else:
      t.goto(x, y)
      t.shape("circle")
      t.color("black")