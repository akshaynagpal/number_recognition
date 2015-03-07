import PIL
from PIL import Image
import numpy as np
from os import listdir
import operator
import pyttsx

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

	vector_to_be_tested = txt2vector('result_4.txt')
##	print "reached here"
##	print labels
	classifier_result = classify0(vector_to_be_tested,trainingMat,labels,3)
	return classifier_result


result = numberClassifier()
print result

engine = pyttsx.init()
engine.setProperty('rate', 70)
engine.say("The number is")
engine.say(str(result))
engine.runAndWait()

    
