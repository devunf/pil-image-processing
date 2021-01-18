from PIL import Image
img = Image.open('images/sunset.png')

nearest_rotate = img.rotate(45, resample=Image.NEAREST, expand=True)
bilinear_rotate = img.rotate(45, resample=Image.BILINEAR, expand=True)
bicubic_rotate = img.rotate(45, resample=Image.BICUBIC, expand=True)

nearest_rotate.save('images/nearest_rotate_sunset.png')
bilinear_rotate.save('images/bilinear_rotate_sunset.png')
bicubic_rotate.save('images/bicubic_rotate_sunset.png') 
