#Script to Recover Fragmented File from Memory Dump

#ImageName: Original File to Recover
#FileName: Memory Dump

#Usage:  python constructImg.py --file <memdump.mem> --image <image name>

import argparse

parser = argparse.ArgumentParser(description='Name of the files to address')

parser.add_argument('--file', dest='FileName', type=str, help='Filename to process')
parser.add_argument('--image', dest='ImageName', type=str, help='Imagename to process')

args = parser.parse_args()

print(args.FileName)
print(args.ImageName)

f = open(args.FileName, 'rb')
fdata = f.read()
f.close()

i = open(args.ImageName, 'rb')
idata = i.read()
i.close()

offsetStart = []
offsetEnd = []

iSize =len(idata)
fSize = len(fdata)

count = 0
startF = 0
startI = 0

while (startI < iSize-100) and (startF < fSize-100):

    if startI + 100 < iSize:
        chunk = idata[startI:startI + 100]
    else:
        break
        
    x1 = fdata.find(chunk, 0)
    if x1 < 0:
        break
    offsetStart.append(x1)
    print('chunk %d fount at offset : %d' % (count, x1))

    startF = x1
    while fdata[startF] == idata[startI]:
        startF += 1
        startI += 1
        if (startI > iSize-1) or (startF > fSize-1):
            break

    x2 = startF
    offsetEnd.append(x2)
    print('End of chunk %d at offset : %d' % (count, x2))
    count += 1

print('chunks found : %d' % count)

img = bytes()
for j in range(count):
    img += fdata[offsetStart[j]:offsetEnd[j]]

fname = 'jpg_images/'+args.ImageName
fw = open(fname, 'wb')
fw.write(img)
fw.close()