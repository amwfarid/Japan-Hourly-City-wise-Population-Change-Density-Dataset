import cv2
import numpy as np
import util

graph = [("before_avg", [255, 0, 0]), ("after_weekday", [0, 255, 255]), ("after_weekend", [0, 0, 255])]

x_origin = 55
x_step = 45
x_scale = 1

y_origin= 694
y_step = 33
y_scale = 2000

input = cv2.imread('input/test2.PNG')
y_origin = input.shape[0] - y_origin

for i in range(len(graph)):

    bgr = graph[i][1]

    line = util.getLine(input,bgr)

    line = util.pixel2Population(line, x_origin, x_step, x_scale, y_origin, y_step, y_scale)

    print(line)

    exit()


