import matplotlib.pyplot as plt
import numpy as np

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0 + 0j  # Initialize z as a complex number
    for _ in range(num_iterations):
        z = z * z + c
        if abs(z) > 2:
            return False
    return True

def mandelbrot(xmin, xmax, ymin, ymax, pixel_density, num_iterations):
    c = complex_matrix(xmin, xmax, ymin, ymax, pixel_density)
    mask = np.frompyfunc(lambda x: is_stable(x, num_iterations), 1, 1)(c)
    return mask.astype(np.bool_)

def plot_mandelbrot(xmin, xmax, ymin, ymax, pixel_density, num_iterations):
    mask = mandelbrot(xmin, xmax, ymin, ymax, pixel_density, num_iterations)
    plt.imshow(mask, extent=(xmin, xmax, ymin, ymax), cmap='gray')
    plt.show()

plot_mandelbrot(-2.5, 1.5, -1.5, 1.5, 1000, 100)
