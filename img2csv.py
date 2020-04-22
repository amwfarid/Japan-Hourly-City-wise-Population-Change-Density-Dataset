import cv2
import util
import pandas as pd
import numpy as np

graph = [("before", [255, 0, 0]), ("after_weekday", [0, 255, 255]), ("after_weekend", [0, 0, 255])]

csv = pd.read_csv('input.csv')

for i in range(len(csv)):

    c = csv.iloc[i]

    input = cv2.imread('input/'+c.city+'.PNG')
    c.y_origin = input.shape[0] - c.y_origin

    for i in range(len(graph)):

        bgr = graph[i][1]

        line = util.getLine(input,bgr)

        line = util.pixel2Population(line, c.x_origin, c.x_step,
                                c.x_scale, c.y_origin, c.y_step,
                                c.y_scale)

        df = pd.DataFrame({'hours':line[:,0],
                           'population':line[:,1]})

        df.to_csv('csv/'+c.city+'_'+graph[i][0]+'.csv',index=False)






