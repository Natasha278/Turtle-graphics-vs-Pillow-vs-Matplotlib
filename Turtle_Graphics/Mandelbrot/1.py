# import turtle as t
# import math

# t.Screen().bgcolor("black")


# #lo primero que debemos hacer es saber si c pertenece al conjunto de mandelbrot
# #Tenemos las condiciones iniciales
# Z_0 = 0

# # La ecuación recursiva del conjunto de mandelbrot
# def Z_n_1(Z_n, c):
#   return Z_n**2 + c

# #Un número máximo de iteraciones
# MAX_ITER = 100

# #Y la función que determina si c pertenece al conjunto de mandelbrot
# def mandelbrot(c):
#   Z_n = Z_0
#   for i in range(0, MAX_ITER):
#     Z_n = Z_n_1(Z_n, c)
#     if abs(Z_n) > 2:
#       return False
#   return True


# #dibujar pixel blanco si c pertenece al conjunto de mandelbrot
# #dibujar pixel
# def paint(x, y, color):
#   pass



# c = x + i*y
# c_2 = x**2 - y**2 + 2*x*y*i

# def z(x, y, n):
#   if n == 0:
#     return (0, 0);

#   val = z(x, y, n - 1)

#   return (val[0] ** 2 - val[1] ** 2 + x, 2 * val[0] * val[1] + y)
  

# sale(x, y):
#   if (z(x, y, MAX_N) > 2:
#     return true
#   else:
#     return false


# for x in range(0, MAX_X):
#   for y in range(0, MAX_Y):
#     if sale(x, y):
#       paint(x, y, white)
#     else:
#       paint(x, y, black)