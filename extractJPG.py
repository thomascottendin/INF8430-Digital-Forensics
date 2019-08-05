#Script to Extract JPG Files

import argparse

parser = argparse.ArgumentParser(description='Name of the file to address')

parser.add_argument('--file', dest='FileName', type=str, help='Filename to process')

args = parser.parse_args()

print(args.FileName)

f=open(args.FileName,'rb')
tdata = f.read()
f.close()

ss = b'\xff\xd8\xff'
se = b'\xff\xd9'

count = 0
start = 0
while True:
    x1 = tdata.find(ss,start)
    if x1 < 0:
        break
    x2 = tdata.find(se,x1)
    y1 = tdata.find(ss,x2+2)
    y2 = tdata.find(se,x2+2)
    while y2 < y1:
        x2 = tdata.find(se,x2+2)
        y1 = tdata.find(ss,x2+2)
        y2 = tdata.find(se,x2+2)
    jpg = tdata[x1:x2+2]
    count += 1
    fname = 'jpg_images/offset-%d-img%s.jpg' % (x1,count)
    fw = open(fname,'wb')
    fw.write(jpg)
    fw.close()
    start = x2 + 3
