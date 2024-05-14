from bb import make_pointss
import cv2
import math


radians = 0.5
pi = 3.14159265
degrees = radians * ( 180.0 / pi )

# Raspberry pi camera width and height
width = 640
height = 480

# Calculate the coordinates of the middel line
# Bottom coordinates
x_bottom = width // 2
y_bottom = height
bottom_point = (x_bottom, y_bottom) 
# Top coordinates
x_top = width // 2
y_top = height // 2
top_point = (x_top, y_top)  

x1, y1, x2, y2 = make_points(frame, line)

#refrens line vector in to <x,y>
class refrens_vector():
    refrens_line_vector_x = x1-x2
    refrens_line_vector_y = y1-y2

rv = refrens_vector()

#middel vector in to <x,y>
class middel_vector():
    middel_vector_x = x_top-x_bottom
    middel_vector_y = y_top-y_bottom

mv = middel_vector
magnitude_of_middel_vector = math.sqrt((mv.middel_vector_x**2) + (mv.middel_vector_y**2))

magnitude_of_refrens_line_vector = math.sqrt((rv.refrens_line_vector_x**2)+(rv.refrens_line_vector_y**2))


def cos_funktion():
    a = middel_vector()
    b = refrens_vector()
    #the dot product of middel_vector and refrens_line_vector
    a*b == [(rv.refrens_line_vector_x)(mv.middel_vector_x)]+[(rv.refrens_line_vector_y)(mv.middel_vector_y)]
    #calculates cos 
    math.cos == a*b / (magnitude_of_middel_vector)(magnitude_of_refrens_line_vector)
    #calculates the angel in degries
    angel = math.acos(math.cos) * (180.0 / math.pi)
    return angel

