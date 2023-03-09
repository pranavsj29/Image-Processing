import cv2 as cv


img = cv.imread('img.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)
#cv.imshow("Alex",resized_img)

gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3)

print(f"no of faces found = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(resized_img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces', resized_img)
cv.waitKey(0)