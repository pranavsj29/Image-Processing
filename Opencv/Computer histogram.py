import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)

blank = np.zeros(resized_img.shape[:2],dtype='uint8')



gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

circle = cv.circle(blank, (resized_img.shape[1]//2,resized_img[0]//2),100,255,-1)


mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('Mask', mask)
# GRayscale histogram
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

plt.figure()
plt.title('Grayscale Histogram')



cv.waitKey(0)

