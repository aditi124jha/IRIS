import cv2
 
img = cv2.imread("ipmage/lilly.jpg")
store = "opimage/eye"
store += "lilly.jpg"
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(img, scaleFactor = 1.2, minNeighbors = 5)
 
 
for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),5)

cv2.imshow("Eye Detected", img)
cv2.imwrite(store, img)
cv2.waitKey(0)
cv2.destroyAllWindows()