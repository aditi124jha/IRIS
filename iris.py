import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as img

def horizontal_edge(width,height,matrix):

    sosm = 3 #size of sq matrix
    vef = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    row=(height-sosm)+1                     #no. of rows it will cover to find out the desired output
    column=(width-sosm)+1                  #no. of columns it will cover to find out the desired output
    result = []
    r = (height-sosm)+1                                         #no. of rows in the output vector
    c = (width-sosm)+1                                         #no. of columns in the output vector
    for i in range(row):
        for j in range(column):
            sq = matrix[i:i+sosm,j:j+sosm]        #slicing
            sum = 0
            for k in range(3):
                for l in range(3):
                    sum += (sq[k,l] * vef[k,l])
            result.append(sum)
    result_matrix = np.asarray(result).reshape(r,c)    #converting to array and reshaping the output matrix
    return result_matrix

def vertical_edge(width,height,matrix):

    sosm = 3
    vef = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
    row=(height-sosm)+1 
    column=(width-sosm)+1 
    result = []
    r = (height-sosm)+1
    c = (width-sosm)+1
    for i in range(row):
        for j in range(column):
            sq = matrix[i:i+sosm,j:j+sosm]
            sum = 0
            for k in range(3):
                for l in range(3):
                    sum += (sq[k,l] * vef[k,l])
            result.append(sum)
    result_matrix = np.asarray(result).reshape(r,c)
    return result_matrix

img = img.imread('rubiks-cube.jpg')
black_n_white = img.mean(axis=2)   #converting to grayscale image
h,w = black_n_white.shape          #shape of the matrix
vertical = vertical_edge(w,h,black_n_white)
horizontal = horizontal_edge(w,h,black_n_white)
image = np.sqrt((vertical**2) + (horizontal**2)) #combining both
plt.imshow(image, cmap='gray', interpolation='nearest') #collecting the final image
plt.show() 