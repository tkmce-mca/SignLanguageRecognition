import cv2
imag=cv2.imread("C:\\Users\\devik\\.spyder-py3\\frame4.jpg")
img=cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img,127,255,0)
M=cv2.moments(thresh)
cx=int(M["m10"]/M["m00"])
cy=int(M["m01"]/M["m00"])
cv2.circle(img,(cx,cy),5,(255,255,255),-1)
cv2.putText(img,"centroid",(cx-25,cy-25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
cv2.imshow("image",img)
cv2.waitKey(0)