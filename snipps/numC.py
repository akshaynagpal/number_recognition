
import PIL
from PIL import Image
import numpy as np
from os import listdir
import operator

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
	print trainingFileList
	m = len(trainingFileList)
	print m
	trainingMat = np.zeros((m,1024))
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		labels.append(classNumStr)
		trainingMat[i,:] = txt2vector("trainingDigits/%s" % fileNameStr)
	print trainingMat

numberClassifier()
