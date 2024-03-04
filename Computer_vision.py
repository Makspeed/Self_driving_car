# import the packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    #Shows half of the screen
    polygon = np.array([[
        (0, height * 1 // 2),
        (width, height * 1 // 2),
        (width, height),
        (0, height),
    ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 100, 200)
    
    cropped_edges = region_of_interest(edges)
    cv2.imshow("Frame", cropped_edges,)
    
    key = cv2.waitKey(1) & 0xFF
    
    rawCapture.truncate(0)
    
    if key == ord("q"):
        break

cv2.destroyAllWindows()