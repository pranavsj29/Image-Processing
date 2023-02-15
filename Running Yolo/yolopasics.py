from ultralytics import YOLO
import cv2
from PIL import Image

model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("Images/1.png", show=True)
cv2.waitKey(0)

