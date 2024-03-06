from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

    

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image
    

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    # Shows half of the screen
    polygon = np.array([[
        (0, height * 1 // 2),
        (width, height * 1 // 2),
        (width, height),
        (0, height),
    ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(edges, mask)
    return masked_image


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    lane_image = np.copy(image) 

    gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5, 5),0)
    canny = cv2.Canny(blur, 100, 200)


    cropped_image = region_of_interest(canny)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    line_image = display_lines(lane_image, lines)
    combine_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

    cv2.imshow("Frame", combine_image)
    
    key = cv2.waitKey(1) & 0xFF
    
    rawCapture.truncate(0)
    
    if key == ord("q"):
        break

cv2.destroyAllWindows()
