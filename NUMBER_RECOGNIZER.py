import os
from os import listdir
import numpy as np
import PIL
from PIL import Image
import pyttsx
import operator
from progressbar import ProgressBar

pbar = ProgressBar()

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
    print sortedClassCount
    return sortedClassCount[0][0]
    
def img2txt(filename,imagedata):
    text_file_name = filename.split('.')[0]+'.txt'
    fo = open(text_file_name,"w")
    for i in range(32):
                for j in range(32):
                        if imagedata[32*i+j] == (255,255,255,255):
                                fo.write('0')
                        else:
                                fo.write('1')
                fo.write('\n')
    fo.close()
    return text_file_name

def txt2vector(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect



file_list = [f for f in os.listdir('./testDigits/') if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.gif')]
print file_list

print "preparing training matrix..."
labels = []
trainingFileList = listdir('trainingDigits')
m = len(trainingFileList)
trainingMat = np.zeros((m,1024))
for i in pbar(range(m)):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        labels.append(classNumStr)
        trainingMat[i,:] = txt2vector("trainingDigits/%s" % fileNameStr)
print "training matrix prepared"


for filename in file_list:
        #display status for each file
        print "working on "+ filename
        #open file
        imgfile=Image.open('testDigits/'+filename)
        #print imgfile.mode
        
        #resize file 32 X 32
        imgfile = imgfile.resize((32,32),PIL.Image.ANTIALIAS)
        #convert to RGBA
        imgfile = imgfile.convert("RGBA")
        #save file
        save_as = filename.split('.')[0] + '_min.png'
        imgfile.save(save_as)
        #get data from image
        img_data = list(Image.open(save_as).getdata())
        #convert to binary text file
        txt_file_name = img2txt(save_as,img_data)
        #make vector from text file data
        file_vector = txt2vector(txt_file_name)
        

        classifier_result = classify0(file_vector,trainingMat,labels,5)

        #audio configurations
        engine = pyttsx.init()
        engine.setProperty('rate', 70)
        engine.say(str(classifier_result))
        #playing audio
        engine.runAndWait()
        #check answer
        reply = raw_input("was the result correct?(y/n)")
        if(reply=='n' or reply=='N'):
            correct_digit = raw_input("Enter the correct digit..")
            check_string = correct_digit+'_'
            check_file_list = [f for f in os.listdir('./trainingDigits/') if f.startswith(check_string)]
            new_file_name = check_string+str(len(check_file_list))+'.txt'
            os.rename(txt_file_name, "trainingDigits/"+new_file_name)
        print "END "+ filename