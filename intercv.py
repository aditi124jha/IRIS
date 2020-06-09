import cv2
import numpy as np
import matplotlib.pyplot as plt

imag=cv2.imread('73931.jpg')
h,w,p=imag.shape
#img=np.zeros([h,w,p],int)
#for x in range (0,h+1):
    #for y in range (0,w+1):
        #for p in range (3):
            #img[x,y,p]=imag[y,x,p]
print ("Current height "+str(h)+" Current width "+str(w))
print ("Enter the scale with which you want to resize the image")
ht=float(input())
wt=float(input())
while True:
        print("\n\n1. Nearest neighbour interpolation\n2. Bilinear interpolation\n3. Bicubic interpolation\n4. Pixel area interpolation\n5. Lanczos interpolation\n\n")
        ch=int(input("Enter your choice : "))
        if ch==1:           #nearest_neighbour
            near_imag=cv2.resize(imag, None, fx=ht, fy=wt, interpolation=cv2.INTER_NEAREST)
            near_img=cv2.cvtColor(near_imag,cv2.COLOR_BGR2RGB)
            plt.imshow(near_img)
            plt.show()
        elif ch==2:           #bilinear
            bilinear_imag = cv2.resize(imag, None, fx=ht, fy=wt, interpolation=cv2.INTER_LINEAR)
            bilinear_img=cv2.cvtColor(bilinear_imag,cv2.COLOR_BGR2RGB)
            plt.imshow(bilinear_img)
            plt.show()
        elif ch==3:           #bicubic
            bicubic_imag=cv2.resize(imag, None, fx=ht, fy=wt, interpolation=cv2.INTER_CUBIC)
            bicubic_img=cv2.cvtColor(bicubic_imag,cv2.COLOR_BGR2RGB)
            plt.imshow(bicubic_img)
            plt.show()
        elif ch==4:           #resampling using pixel area relation
            area_imag=cv2.resize(imag, None, fx=ht, fy=wt, interpolation=cv2.INTER_AREA)
            area_img=cv2.cvtColor(area_imag,cv2.COLOR_BGR2RGB)
            plt.imshow(area_img)
            plt.show()
        elif ch==5:           #Lanczos interpolation over 8×8 pixel neighborhood
            lanc_imag=cv2.resize(imag, None, fx=ht, fy=wt, interpolation=cv2.INTER_LANCZOS4)
            lanc_img=cv2.cvtColor(lanc_imag,cv2.COLOR_BGR2RGB)
            plt.imshow(lanc_img)
            plt.show()
        else:
            print("Wrong Choice!! Try again!")
            
main()