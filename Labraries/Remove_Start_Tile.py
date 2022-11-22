import numpy as np
import cv2 as cv


def run_for_all_thresh(start_tile, thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine):
    matrix_2d = np.zeros((5, 5))

    def remove_start_tile_for_thresh(thresh):

        for y in range(len(start_tile[:, 0])):
            for x in range(len(start_tile[0, :])):
                if start_tile[x, y] >= 1:
                    thresh[x, y] = 0
        return thresh

    thresh_grass = remove_start_tile_for_thresh(thresh_grass)
    thresh_woods = remove_start_tile_for_thresh(thresh_woods)
    thresh_water = remove_start_tile_for_thresh(thresh_water)
    thresh_desert = remove_start_tile_for_thresh(thresh_desert)
    thresh_dirt = remove_start_tile_for_thresh(thresh_dirt)
    thresh_mine = remove_start_tile_for_thresh(thresh_mine)

    # print(start_tile)
    # print(thresh_dirt)

    #TODO: OUTPUT IMAGE HERE

    # Making an output image to see where the tile are
    # def last_tile_image(thresh, color):
    #     for y in range(len(thresh[:, 0])):
    #         for x in range(len(thresh[0, :])):
    #             if thresh[x, y] == 255:
    #                 matrix_2d[x, y][0] = thresh[x, y][0]
    #
    # matrix_2d = np.zeros((5, 5))
    #
    # # grass_image = last_tile_image(thresh_grass, 255)
    # woods_image = last_tile_image(thresh_woods, 255)
    # # water_image = last_tile_image(thresh_water)
    # # desert_image = last_tile_image(thresh_desert)
    # # dirt_image = last_tile_image(thresh_dirt)
    # # mine_image = last_tile_image(thresh_mine)
    #
    # cv.imshow("TEST", matrix_2d)

    return thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine
