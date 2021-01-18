from PIL import Image
img = Image.open('images/image.png').convert('LA')
img.save('images/greyscale.png')
