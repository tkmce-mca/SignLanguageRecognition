23-09-2019

Calculating frame difference, Correction on program logic

import cv2 
import os 

# Read the video from specified path 
cam = cv2.VideoCapture("C:\\Users\\devik\\.anaconda\\navigator\\Areyouhungry.mp4") 
f=[]

try: 
	
	
	if not os.path.exists('data'): 
		os.makedirs('data')  
except OSError: 
	print ('Error: Creating directory of data') 

# frame 
currentframe = 0

while(True): 
	
	# reading from frame 
	ret,frame = cam.read() 

	if ret: 
		# if video is still left continue creating images 
		name = './data/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name)
        
        
		# writing the extracted images 
		cv2.imwrite(name, frame) 
        f.append(frame)
		# increasing counter so that it will 
		# show how many frames are created 
		currentframe += 1
	else: 
		break

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
