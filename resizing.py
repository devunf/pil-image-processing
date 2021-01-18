from PIL import Image
img = Image.open('images/sunset.png')
size = (350, 550)
nearest_resize = img.resize(size, 0)
lanczos_resize = img.resize(size, 1)
bilinear_resize = img.resize(size, 2)
bicubic_resize = img.resize(size, 3)

nearest_resize.save('images/nearest_sunset.png')
lanczos_resize.save('images/lanczos_sunset.png')
bilinear_resize.save('images/bilinear_sunset.png')
bicubic_resize.save('images/bicubic_sunset.png') 
