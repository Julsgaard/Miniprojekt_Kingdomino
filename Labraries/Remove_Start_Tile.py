import numpy as np
import cv2 as cv


def run_for_all_thresh(start_tile, thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine):

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


    return thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine
