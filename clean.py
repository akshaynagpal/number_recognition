import os
filelist = [f for f in os.listdir('.') if f.endswith('_min.png') or f.endswith('_min.txt')]

for f in filelist:
    os.remove(f)
