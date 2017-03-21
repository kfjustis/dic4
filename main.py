import sys
import getopt
import numpy as np
from PIL import Image
import numpy

'''
Loads an image from given file path
and stores it as an array. Used for
grayscale only -- other images untested

// param:  imgFile - the file path for a given
//         image to be loaded
// return: an array of numbers between 0-255
//         representing the given image file
'''
def load_image_as_array(imgFile):
	img = Image.open(imgFile)
	imgArray = numpy.asarray(img)

	return imgArray

def print_image_array(imgArr):
	if imgArr is not None:
		print(imgArr)

def main(argv):
	inputFile = ""

	# load file with command line args
	try:
		opts, args = getopt.getopt(argv, "i:")
	except getopt.GetoptError:
		print("USAGE: python3 main.py -i <input file>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-i":
			inputFile = arg
		else:
			print("USAGE: python3 main.py -i <input file>")
			sys.exit()

	if (inputFile is ""):
		print("USAGE: python3 main.py -i <input file>")
		sys.exit()

	imgArr = load_image_as_array(inputFile)
	print("Image loaded!")
	print_image_array(imgArr)

if __name__ == "__main__":
	main(sys.argv[1:])
