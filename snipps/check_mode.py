import PIL
from PIL import Image
image_name = raw_input("enter name of image to open!")
imgfile=Image.open(image_name)
print imgfile.mode
raw_input()
