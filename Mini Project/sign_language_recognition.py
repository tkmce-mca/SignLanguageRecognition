import cv2
import os
# Read the video from specified path
cam=cv2.VideoCapture("C:\\Users\\devik\\.anaconda\\navigator\\Allthebest.mp4")
x=0
y=0
os.makedirs('extracted')
os.makedirs('extractedimgframe')
try:
    # creating folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
# if not created then raise error
except OSError:
    print('error')
# Frame
currentframe=0
while(True):
    
    # reading from frame
    ret,frame=cam.read()
    if ret:
        # oif video is still left continue creating images
        name='./data/frame' + str(currentframe) + '.jpg'
        print('creating...' +name)
        # writing extracted images
        cv2.imwrite(name,frame)
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# convert grayscale image into binary image
        ret,thresh=cv2.threshold(img,127,255,0)
# calculate moments of binary image
        M=cv2.moments(thresh)
# calculate x,y coordinayes of center
        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])
        print(cx)
        print(cy)
# put text and highlight the center
        cv2.circle(img,(cx,cy),5,(255,255,255),-1)
        cv2.putText(img,"centroid",(cx-25,cy-25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
# display the image
        cv2.imshow("image",img)
        cv2.waitKey(0)
        print(x)
        print(y)
        if cx==x and cy==y:
           print("No change in centroid")
        else:
            print("Change in centroid")
            #cv2.imshow("image",img)
            #cv2.waitKey(0)
        # extract frames having change in centroid
            name1='./extracted/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name1,frame)
        #create threshold value to extract significant frames
            if cx==316 and 166<=cy<=167:
                name2='./extractedimgframe/frame' + str(currentframe) + '.jpg'
                cv2.imwrite(name2,frame)
            
            
    # increasing counter
        currentframe+=1
        x=cx
        y=cy
        
        
    else:
        break
            
cam.release()
cv2.destroyAllWindows
