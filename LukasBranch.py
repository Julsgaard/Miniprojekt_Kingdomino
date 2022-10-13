import cv2 as cv
import numpy as np

# Importing image "board20" and getting an output
#

input_image = cv.imread("20.jpg")

def slice_IMG(input_image):
    output = []
    for y in range(0, input_image.shape[0], int(input_image.shape[0]/5)):
        yLine = []
        for x in range(0, input_image.shape[1], int(input_image.shape[1]/5)):
            slice = input_image[y: y + int(input_image.shape[0]/5), x:x + int(input_image.shape[1]/5)]
            yLine.append(slice)
    output.append(yLine)
    return output

tile = slice_IMG(input_image)
cv.imshow('output_image', tile[0][0])
cv.waitKey(0)




