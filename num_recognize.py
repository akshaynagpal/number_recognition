import PIL
from PIL import Image
import numpy as np
from os import listdir
import operator

text_file_name = ''

def classify0(inX, dataSet, labels, k):
	# inX - input vector to classify
	# dataSet - training examples
	# labels - vector of lables
	# k - no.of nearest neghbours to use 
	dataSetSize = dataSet.shape[0] #shape[0] gives no. of rows
	diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
	#numpy.tile(A, reps)
	#Construct an array by repeating A the number of times given by reps.
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	# print distances
	sortedDistIndices = distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel = labels[sortedDistIndices[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	# print classCount
	# print sortedClassCount
	return sortedClassCount[0][0]

def img2txt(filename):
	print filename + "img2txt"
	img = Image.open(filename)
	x = list(img.getdata())
	print 'HEREE IS THE IMG DATA'
	for k in x:
	        print k
	global text_file_name
	text_file_name = filename.split('_')[0]+'.txt'
	fo = open(text_file_name,"w")

	for i in range(32):
		for j in range(32):	
			if x[32*i+j] < (0,0,0,128):
				fo.write('0')
			else:
				fo.write('1')
		fo.write('\n')
	fo.close()
	return 1

def txt2vector(filename):
	returnVect = np.zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect

def numberClassifier():
	labels = []
	trainingFileList = listdir('trainingDigits')
	# print trainingFileList
	m = len(trainingFileList)
	# print m
	trainingMat = np.zeros((m,1024))
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		labels.append(classNumStr)
		trainingMat[i,:] = txt2vector("trainingDigits/%s" % fileNameStr)
		#testFileList = listdir('testDigits')
	global text_file_name	
	vector_to_be_tested = txt2vector(text_file_name)
	# print "reached here"
	# print labels
	classifier_result = classify0(vector_to_be_tested,trainingMat,labels,3)
	return classifier_result

image_name = raw_input("enter name of image to open!")

#resizing the image to 32 X 32 pixels

img = Image.open(image_name)
print img.mode
img = img.resize((32,32),PIL.Image.ANTIALIAS)
save_as = image_name.split('.')[0] + '_small.png'
img.save(save_as)

if img2txt(save_as)==1:
	print "image converted to txt successfully!"

print "number in the image identified as: "
print numberClassifier()

raw_input()
