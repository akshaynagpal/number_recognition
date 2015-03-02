import PIL
from PIL import Image
image_name = raw_input("enter name of image to open!")
imgfile=Image.open(image_name)
imgfile = imgfile.resize((32,32),PIL.Image.ANTIALIAS)
print imgfile.mode
print imgfile.size
data1 = list(imgfile.getdata())
for i in range(32):
    for j in range(32):
        print str(i) + " " + str(j)+" " +str(data1[32*i+j])

imgfile = imgfile.convert("RGBA")
#imgfile = imgfile.resize((32,32),PIL.Image.ANTIALIAS)
save_as = image_name.split('.')[0] + '_min.png' #+ image_name.split('.')[1]
print save_as
imgfile.save(save_as)
print "mode :",imgfile.mode

data2 = list(imgfile.getdata())
for i in range(32):
    for j in range(32):
        print str(i) + " " + str(j)+" " +str(data2[32*i+j])
print imgfile.mode

text_file_name = 'result.txt'
fo = open(text_file_name,"w")
for i in range(32):
        for j in range(32):	
                if data2[32*i+j] == (255,255,255,255):
                        fo.write('0')
                else:
                        fo.write('1')
        fo.write('\n')
fo.close()
##imgfile = imgfile.convert('L')
##print imgfile.mode
##idata = list(imgfile.getdata())
##for i in range(32):
##    for j in range(32):
##        print str(i) + " " + str(j)+" " +str(idata[32*i+j])
# bw = gray.point(lambda x: 0 if x<128 else 255, '1')
# bw.save("result_bw.png")
# bw.show()
# gray.show() 
