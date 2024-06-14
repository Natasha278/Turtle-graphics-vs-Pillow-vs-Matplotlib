from PIL import Image, ImageDraw

# Image dimensions and pixels of the computer
width, height = 1500, 900

# Create a new image with white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

#Number of iterations
max_iter = 100

# Drawing Mandelbrot set
for x in range(width):
    for y in range(height):
        # Adjust Scale x and y, it will depend on the pixels choosed
        re = (x / width)*4 - 2.5
        im = (y / height)*2 - 1
        c = complex(re, im)
        z = 0 + 0j
        is_in_set = True
        for n in range(max_iter):
            z = z*z + c
            if abs(z) > 2:
                is_in_set = False
                draw.point([x, y], "white")
                break
        if is_in_set:
            draw.point([x, y], (0, 0, 0))

# Save and show the image
image.save("mandelbrot.png")
image.show()
