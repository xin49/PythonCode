import os, glob
from PIL import Image

img = Image.open("1.jpg")
img = img.rotate(90)
img.show()
