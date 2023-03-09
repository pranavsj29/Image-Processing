import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)

blank = np.zeros(resized_img.shape[:2],dtype='uint8')
cv.imshow("Blank Image", blank)

mask = cv.circle(blank , (resized_img.shape[1]//2 , resized_img.shape[0]//2),100,255,-1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(resized_img, resized_img, mask=mask)
cv.imshow("Masked img", masked)

cv.waitKey(0)