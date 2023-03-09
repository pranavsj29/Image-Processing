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

#Translation of image
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return  cv.warpAffine(img,transMat,dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y -->Down

translated = translate(resized_img,50,50)
cv.imshow("translated img", translated)

#Rotation of image
def rotate (img,angle , rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(resized_img,45)
cv.imshow("Rotated",rotated)

# Resizing

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resized)


#Flipping
flip = cv.flip(resized_img,0)
cv.imshow("FLipped img",flip)
# 0 -->flip img vertically
# 1 --> flip img horizontally
# -1 --> flip img both vertically and horizontally

cv.waitKey(0)