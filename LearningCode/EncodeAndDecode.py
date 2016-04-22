# coding: UTF-8
import os, PIL
from PIL import Image

def LoadImage(ImageName):
	img=Image.open(ImageName.decode('UTF-8'))
	img.show()

if __name__=='__main__':
	ImageName='测试图片.jpg'
	ImageNameAnsi=ImageName.encode('UTF-8')
	print ImageNameAnsi
	LoadImage(ImageName)

#decode('now data code type') and encode('want to encode type') 
