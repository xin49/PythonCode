import os, glob
from PIL import Image

if __name__=='__main__':
	try:
		img = Image.open("1.jpg")
		img = img.rotate(90)
		img.show()
	finally:
		os.system('pause')

