from PIL import Image
imgfile=Image.open('C:\/Users\/advance\/Documents\/GitHub\/data_science\/image_manipulation\/snipps\/1_small.png')
print imgfile.mode
data = list(imgfile.getdata())
for i in range(32):
    for j in range(32):
        print str(i) + " " + str(j)+" " +str(data[32*i+j])
print imgfile.mode
imgfile = imgfile.convert('L')
print imgfile.mode
imgfile = imgfile.convert("RGBA")
print imgfile.mode
idata = list(imgfile.getdata())
for i in range(32):
    for j in range(32):
        print str(i) + " " + str(j)+" " +str(idata[32*i+j])
# bw = gray.point(lambda x: 0 if x<128 else 255, '1')
# bw.save("result_bw.png")
# bw.show()
# gray.show() 
