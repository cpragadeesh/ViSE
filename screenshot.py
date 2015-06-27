import cv2.cv as cv
import time

video = cv.CaptureFromFile('/path/of/video/1.mp4')
frame = int( cv.GetCaptureProperty(video,cv.CV_CAP_PROP_FRAME_COUNT))
i = 1
no = 1

while (i<frame):
	img = cv.QueryFrame(video)
	cv.SaveImage("img/"+str(no)+".jpg",img)
	no = no + 1
	i = i + 60 #screenshot every 60 frames

cv.DestroyAllWindows() #not necessary