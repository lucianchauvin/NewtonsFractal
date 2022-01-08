from PIL import Image
import math

width = 1500
height = 1100

img  = Image.new(mode = "RGB", size = (width, height) )

pixels = img.load()
maxint = 50
tolerance = 0.000001


roots = [1,complex(-1/2, (math.sqrt(3)/2)), complex(-1/2, -1*(math.sqrt(3)/2))]
colors = [(255,0,0),(0,255,0),(0,0,255)]

def function(z):
    return z**3 - 1

def derivitive(z):
    return 3*z**2

def rescale(val, in_min, in_max, out_min, out_max):
    return out_min + (val - in_min) * ((out_max - out_min) / (in_max - in_min))

for y in range(height):
    for x in range(width):
        print(str(round(100*y/height,1)) + "% done")
        zx = rescale(x, 0, width, -2.5, 1)
        zy = rescale(y, 0, height, -1, 1)

        z = complex(zx, zy)
        for h in range(maxint):
            z -= function(z)/derivitive(z)
            for p in range(len(roots)):
                if abs((z - roots[p]).real) < tolerance and abs((z - roots[p]).imag) < tolerance:
                    pixels[x,y] = colors[p]
                    break
                else:
                    pixels[x,y] = ((0,0,0))

img.show()