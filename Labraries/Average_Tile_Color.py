import numpy as np
import cv2 as cv

"""
Slice_IMG makes 5 times 5 slices of the input image
"""


def slice_IMG(input_image):
    output = []
    for y in range(0, input_image.shape[0], int(input_image.shape[0] / 5)):
        yLine = []
        for x in range(0, input_image.shape[1], int(input_image.shape[1] / 5)):
            slice = input_image[y: y + int(input_image.shape[0] / 5), x: x + int(input_image.shape[1] / 5)]
            yLine.append(slice)
        output.append(yLine)

    return output


def slice_img(img):
    M = img.shape[0] // 5
    N = img.shape[1] // 5

    print(M, N)

    tiles = [img[x:x + M, y:y + N] for x in range(0, img.shape[0], M) for y in range(0, img.shape[1], N)]

    print(tiles)

    cv.imshow("tilesss", tiles)
    cv.waitKey(0)

    return output


# TODO: Make simpler
def get_dominant_colour(tile):
    tile_colors = []
    for i in range(len(tile)):
        for j in range(len(tile[i])):
            data = np.reshape(tile[i][j], (-1, 3))
            data = np.float32(data)

            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            flags = cv.KMEANS_RANDOM_CENTERS
            compactness, labels, centers = cv.kmeans(data, 1, None, criteria, 10, flags)

            color = centers[0].astype(np.int32)
            # print(f'Dominant color is: bgr({color})')
            tile_colors.append(color)

    return tile_colors


def get_average_color(img: np.ndarray):
    # print(len(tile[1]))
    width, height = img.shape[0], img.shape[1]

    blue, green, red = 0, 0, 0
    for x in range(width):
        for y in range(height):
            # print(f"{x},{y}")
            blue += img[x, y, 0]
            green += img[x, y, 1]
            red += img[x, y, 2]

    # Calculates the average color
    blue /= width * height
    green /= width * height
    red /= width * height
    for x in range(width):
        for y in range(height):
            img[x, y, 0] = blue
            img[x, y, 1] = green
            img[x, y, 2] = red

    print(blue, red, green)
    return blue, red, green


def set_tile_color(tile_colors):
    matrix1D = np.zeros((25, 1, 3), dtype=np.uint8)

    for i in range(len(matrix1D)):
        matrix1D[i, 0, 0] = tile_colors[i][0]
        matrix1D[i, 0, 1] = tile_colors[i][1]
        matrix1D[i, 0, 2] = tile_colors[i][2]

    # Getting list with hsv for tiles
    output = []
    tile_colors_to_hsv = cv.cvtColor(matrix1D, cv.COLOR_BGR2HSV)
    # print(tile_colors_to_hsv)

    matrix2D = np.reshape(matrix1D, (5, 5, 3))

    return matrix2D


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

# customIMG = np.zeros((7, 7), dtype=int)


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
