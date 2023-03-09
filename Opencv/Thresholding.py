import cv2 as cv

img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)
#cv.imshow("resized img",resized_img)

gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
threading,thresh = cv.threshold(gray,200,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

threading,thresh_inv = cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold inverse',thresh_inv)

# Adoptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding ", adaptive_thresh)



cv.waitKey(0)