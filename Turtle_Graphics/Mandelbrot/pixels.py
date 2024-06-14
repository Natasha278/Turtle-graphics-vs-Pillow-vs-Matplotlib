import turtle
from PIL import Image, ImageDraw

# Image dimensions
width, height = 1500, 900

# Create a new image with white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Number of iterations for checking if a point is in the Mandelbrot set
max_iter = 100

# Check if the complex number c is in the set
def is_in_set(c):
    #define initial condition
    z = 0 + 0j
    for _ in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return False
    return True

# Drawing Mandelbrot set
#iterate for each withd pixel
for x in range(width):
    #iterate for each height pixel
    for y in range(height):
        # Adjust x and y to correspond to the complex plane coordinates
        re = (x / width) * 4 - 2.5
        im = (y / height) * 2 - 1
        # re-name c
        c = complex(re, im)
        if is_in_set(c):
            draw.point([x, y], "black")
        else:
            draw.point([x, y], "white")

# Save and show the image
image.save("mandelbrot.png")
image.show()
