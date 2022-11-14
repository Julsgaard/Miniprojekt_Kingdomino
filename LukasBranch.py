import numpy as np
import cv2 as cv
from collections import deque


# Importing image "board20" and getting an output

"""
Loading input image
"""

input_image = cv.imread("20.jpg")

"""
Slice_IMG makes 5 times 5 slices of the input image
"""
def slice_IMG(input_image):
    output = []
    for y in range(0, input_image.shape[0], int(input_image.shape[0]/5)):
        yLine = []
        for x in range(0, input_image.shape[1], int(input_image.shape[1]/5)):
            slice = input_image[y: y + int(input_image.shape[0]/5), x: x + int(input_image.shape[1]/5)]
            yLine.append(slice)
        output.append(yLine)
    return output


"""
We get the mean R,G,B values for all the slices in the input image
"""

def average_RGB(tile):
    averageBGR = np.average(tile, axis=0)
    average_averageBGR = np.average(averageBGR, axis=0)
    return average_averageBGR


"""
Creating custom image the same size as input image, which is 5 times 5 + 2 in each row 
if we want to use a 4 connectivity grassfire later on to avoid getting the " out of bounce" message 
"""

customIMG = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

"""
We assign numbers to each possible field variation
"""



crownField = 1
mine = 2
water = 3
Desert = 4
grassLand = 5
woodLand = 6
dirtLand = 7

"""
We need a grassfire function to check how many similar fields lie close to each other and assigns points accordingly
"""
"""
def ignite_pixel(image, coordinate, id):
    y, x = coordinate
    burn_queue = deque()

    if image[y, x] == 1 or 2 or 3 or 4 or 5 or 6 or 6 or 7:
        burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        if image[y, x] == 1 or 2 or 3 or 4 or 5 or 6 or 6 or 7:
            image[y, x] = id

            if x + 1 < image.shape[1] and image[y, x + 1] == 1 or 2 or 3 or 4 or 5 or 6 or 6 or 7:
                burn_queue.append((y, x + 1))
            if y + 1 < image.shape[0] and image[y + 1, x] == 1 or 2 or 3 or 4 or 5 or 6 or 6 or 7:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and image[y, x - 1] == 1 or 2 or 3 or 4 or 5 or 6 or 6 or 7:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and image[y - 1, x] == 1 or 2 or 3 or 4 or 5 or 6 or 6 or 7:
                burn_queue.append((y - 1, x))

        #print(image)
        #print(burn_queue)
        #input()

        if len(burn_queue) == 0:
            return id + 50

    return id


def grassfire(image):
    next_id = 50
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(image, (y, x), next_id)

grassfire(img)
"""


"""
Function calls
"""

tile = slice_IMG(input_image)
tileBGR_average = average_RGB(tile)
print(tileBGR_average)
cv.imshow('output_image', tile[0][0])
cv.imshow('20.jpg', input_image)
cv.waitKey(0)







