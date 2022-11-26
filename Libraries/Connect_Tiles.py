import cv2 as cv


def connect_tile(thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine):
    connected_grass = cv.connectedComponents(thresh_grass, 4, cv.CV_32S)
    connected_woods = cv.connectedComponents(thresh_woods, 4, cv.CV_32S)
    connected_water = cv.connectedComponents(thresh_water, 4, cv.CV_32S)
    connected_desert = cv.connectedComponents(thresh_desert, 4, cv.CV_32S)
    connected_dirt = cv.connectedComponents(thresh_dirt, 4, cv.CV_32S)
    connected_mine = cv.connectedComponents(thresh_mine, 4, cv.CV_32S)

    return connected_grass[1], connected_woods[1], connected_water[1], connected_desert[1], connected_dirt[1], \
           connected_mine[1]
