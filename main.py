import cv2
import numpy as np

img=cv2.imread('test.png')

def equ(a,b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True

def isColor(c):
    f=lambda x:x<50 and x>10
    return f(c[0]) and f(c[1]) and c[2]>220

x1=(146-92)/10

xStart=330 # 写生起点， 自己指定
xMax=576
y0=410
x0=80
yKnow=332 # 0上面一个区间点的坐标，自己指定
yKnowVal=10 # 0上面一个坐标点的值，自己指定
y1=(y0-yKnow)/yKnowVal
yMax=58

allX=[]
allY=[]

x=xStart
lastAppendX=None
while x<xMax:
    for y in range(yMax,y0):
        xi = int(x)
        if xi!=lastAppendX and isColor(img[y, xi]):
            xReal = (xi - x0) / x1
            if xReal != lastAppendX:
                allX.append(xReal)
                lastAppendX = xReal
                yReal=(y0 - y) / y1
                allY.append(yReal)
                print(xReal,yReal)
    x+=x1

import cubic
f=cubic.cubic(allX,allY)

dayStart=int((xStart-x0)/x1) # 预测起始天（坐标图中x坐标）
dayEnd=90 # 预测结束天（坐标图中x坐标），自己指定

allPos=[]
zeroPos=-1
nonZeroVal=-1
for day in range(dayStart,dayEnd+1):
    y=int(f(day))
    if nonZeroVal==-1 and y==0:
        zeroPos=day-dayStart # 前面最后一个0下标是多少
    if nonZeroVal==-1 and y!=0:
        nonZeroVal=y # 第一个非0的预测值
    allPos.append([day,y])

for i in range(zeroPos+1): # 前面的0修正
    allPos[i][1]=nonZeroVal # 修正y值为第一个y非0值

allPos=np.array(allPos)
np.savetxt('result.csv',allPos,fmt='%d',delimiter=',')