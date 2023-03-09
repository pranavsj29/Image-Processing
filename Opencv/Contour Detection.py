import cv2 as cv
import numpy as np
img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)
#cv.imshow('Image',resized_img)

blank = np.zeros(resized_img.shape,dtype='uint8')

gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# canny = cv.Canny(resized_img,125,175)
# cv.imshow('Canny',canny)

ret , thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)


contours , hierachies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)}contours(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contours Dawn', blank)

cv.waitKey(0)