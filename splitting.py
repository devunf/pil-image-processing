from PIL import Image
import numpy

img = Image.open('images/sunset.png')
data = img.getdata()

red = [(pixel[0], 0, 0) for pixel in data]
green = [(0, pixel[1], 0) for pixel in data]
blue = [(0, 0, pixel[2]) for pixel in data]

img.putdata(red)
img.save('images/red_sunset.png')
img.putdata(blue)
img.save('images/blue_sunset.png')
img.putdata(green)
img.save('images/green_sunset.png')
