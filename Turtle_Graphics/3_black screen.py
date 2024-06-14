import turtle as t

#Draw 3
drawing_area = t.Screen()
#name of the graphics window
drawing_area.title("Mandelbrot Set")
drawing_area.bgcolor("black")
#empieza desde las esquina izquierda
drawing_area.setup(width=1700, height=900, startx=0, starty=0)
t.exitonclick()