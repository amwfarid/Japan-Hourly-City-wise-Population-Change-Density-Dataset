import cv2
import numpy as np

def getLine(input, bgr):

    lower = np.array(bgr)
    upper = np.array(bgr)
    mask = cv2.inRange(input, lower, upper)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        if len(c) > 1500:
            mask = np.zeros(input.shape, np.uint8)
            cv2.drawContours(mask, c, -1, (255, 255, 255), 3)
            break

    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    line = np.zeros(mask.shape[1])

    for i in range(mask.shape[1]):
        for j in range(mask.shape[0]):
            if mask[j][i] == 255:
                line[i] = (mask.shape[0] - j) + 3
                break

    return line

def pixel2Population(line, x_origin, x_step, x_scale, y_origin, y_step, y_scale):

    new_line = np.zeros((24,2))

    for i in range(24):

        x = x_origin +(x_step*i)
        y = line[x]

        population = (y-y_origin) * (y_scale/y_step)

        hour = (((x-x_origin)/x_step)+13)%24

        new_line[i][0] = hour
        new_line[i][1] = population

    return new_line