import sys
import getopt
import numpy
import matplotlib.pyplot as plt
from PIL import Image

numpy.set_printoptions(threshold=numpy.nan)

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

	# load image as array
	print("Loading image...")
	imgArr = load_image_as_array(inputFile)
	print("Image loaded!")

	# determine the correlation matrix
	print("Finding correlation matix...")
	i = 0
	j = 0
	maxInd = 512
	cx = numpy.zeros((512,512))
	numpy.reshape(imgArr, (512,512))
	for i in range(0, maxInd):
		for j in range(0, maxInd-1):
			cx[i][j] = (int(imgArr[i][j]) * int(imgArr[i][j+1])) / 2

	# get U, s, V
	print("Doing decomposition...")
	U, s, V = numpy.linalg.svd(cx)
	print("Transform found!")

	# plot U column vectors with slicing
	print("Graphing...")
	i = 0
	#x = U[:,i]
	#y = U[i,:]
	for i in range(0, 16):
		plt.stem(U[i,:], linefmt='-', markerfmt='o')
		plt.savefig('vec'+str(i)+'.png', bbox_inches='tight')
		plt.clf()

	# show plot
	#plt.show()

if __name__ == "__main__":
	main(sys.argv[1:])
