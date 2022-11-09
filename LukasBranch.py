import cv2 as cv
import numpy as np
import cv2 as cv

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
            slice = input_image[y: y + int(input_image.shape[0]/5), x:x + int(input_image.shape[1]/5)]
            yLine.append(slice)
    output.append(yLine)
    return output


"""
We get the mean R,G,B values for all the slices in the input image
"""

def mean_RGB(yLine):
   meanBGR = np.mean(yLine, axis = 0)
   mean_meanBGR = np.mean(meanBGR, axis = 0)
   return mean_meanBGR


"""
Creating custom image the same size as input image, which is 5 times 5 + 2 in each row 
if we want to use a 4 connectivity grassfire later on to avoid getting the " out of bounce" message 
"""

customIMG = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

"""
We assign numbers to each possible field variation
"""

crownField = 0
mine = 1
water = 2
Desert = 3
grassLand = 4
woodLand = 5
dirtLand = 6


"""
We need a grassfire function to check how many similar fields lie close to each other and assigns points accordingly
"""

tile = slice_IMG(input_image)
tileBGR_Mean = mean_RGB(tile)
print(tileBGR_Mean)
cv.imshow('output_image', tile[0][0])
cv.imshow('20.jpg', input_image)
cv.waitKey(0)







