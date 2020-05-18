import matplotlib.image as img 
import matplotlib.pyplot as plt
import numpy as np
import math

imag = img.imread('73931.jpg')
h,w,p= imag.shape
print ("Current height "+str(h)+" Current width "+str(w))
print ("Enter new height and width")
height=int(input())
width=int(input())
newimg=np.zeros([height,width,p],int)
scaley=w/width
scalex=h/height

for x in range (height):
    for y in range (width):
        for p in range (3):
            newimg[x,y,p]=imag[int(math.floor(scalex*x))][int(math.floor(scaley*y))][p]

plt.imshow(newimg)
plt.show()