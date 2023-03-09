import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)

blank = np.zeros(resized_img.shape[:2], dtype='uint8')
b,g,r = cv.split(resized_img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)



# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

print("resize = ", resized_img.shape)
print("b = ", b.shape)
print("g = ", g.shape)
print("r = ", r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)

cv.waitKey(0)