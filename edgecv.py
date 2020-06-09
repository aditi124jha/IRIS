import cv2

img=cv2.imread("r.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(3,3),0)
edges=cv2.Canny(img, threshold1=30, threshold2=100)
store = "opimage/edge"
store += "celeb.jpg"

cv2.imshow('image',edges)
cv2.imwrite(store, edges)
cv2.waitKey(0)
cv2.destroyAllWindows()