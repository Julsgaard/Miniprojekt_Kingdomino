import numpy as np


def output_image(thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine):
    h, w, = thresh_desert.shape
    output = np.zeros((h, w, 3), dtype=np.uint8)

    for x in range(len(thresh_desert)):
        for y in range(len(thresh_desert[x])):
            # Makes all tiles white
            output[x, y, 0] = 255
            output[x, y, 1] = 255
            output[x, y, 2] = 255

            # Give the tiles a designated color if the thresh has a white dot in x,y
            if thresh_grass[x, y] >= 255:
                output[x, y, 0] = 37
                output[x, y, 1] = 153
                output[x, y, 2] = 103
            if thresh_woods[x, y] >= 255:
                output[x, y, 0] = 16
                output[x, y, 1] = 67
                output[x, y, 2] = 55
            if thresh_water[x, y] >= 255:
                output[x, y, 0] = 162
                output[x, y, 1] = 96
                output[x, y, 2] = 4
            if thresh_desert[x, y] >= 255:
                output[x, y, 0] = 19
                output[x, y, 1] = 173
                output[x, y, 2] = 178
            if thresh_dirt[x, y] >= 255:
                output[x, y, 0] = 67
                output[x, y, 1] = 117
                output[x, y, 2] = 131
            if thresh_mine[x, y] >= 255:
                output[x, y, 0] = 26
                output[x, y, 1] = 20
                output[x, y, 2] = 28

    return output
