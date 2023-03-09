import cv2 as cv
import numpy as np


img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)
#cv.imshow("resized img", resized_img)

gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

# Sabel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,00,1)
combined_sobel = cv.bitwise_or(sobelx , sobely)

cv.imshow("Sabel x", sobelx)
cv.imshow("Sabel y", sobely)
cv.imshow('Combined Soble', combined_sobel)


canny = cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

cv.waitKey(0)