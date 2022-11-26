import cv2 as cv


def tile_threshold(combined_tiles):

    #Converting image from BGR to HSV colorspace
    combined_tiles_HSV = cv.cvtColor(combined_tiles, cv.COLOR_BGR2HSV)

    # Hue is divided with 2 because the website we used, shows the value from 0-360 but OpenCV uses 0-180
    # Saturation and value is multiplied with 2.55 because the website shows from 0-100.
    # Website used to find the HSV range: https://redketchup.io/color-picker

    # OpenCV range: Hue 0-180, Saturation 0-255, Value 0-255
    thresh_grass = cv.inRange(combined_tiles_HSV, (60/2, 60*2.55, 28*2.55), (100/2, 100*2.55, 70*2.55))
    thresh_woods = cv.inRange(combined_tiles_HSV, (61/2, 0*2.55, 13*2.55), (255/2, 255*2.55, 28*2.55))
    thresh_water = cv.inRange(combined_tiles_HSV, (195/2, 75*2.55, 30*2.55), (220/2, 105*2.55, 80*2.55))
    thresh_desert = cv.inRange(combined_tiles_HSV, (40/2, 85*2.55, 50*2.55), (60/2, 105*2.55, 90*2.55))
    thresh_dirt = cv.inRange(combined_tiles_HSV, (35/2, 14*2.55, 28*2.55), (55/2, 70*2.55, 60*2.55))
    thresh_mine = cv.inRange(combined_tiles_HSV, (22/2, 0*2.55, 5*2.55), (61/2, 70*2.55, 28*2.55))

    return thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine



"""
Crown field nr: 13
Water tiles nr: 1,2,3,4,5,10,15,20
Mine tiles nr: 11, 16, 17
Desert tiles nr: 21, 22, 23, 24, 25
Grass tiles nr: 8, 18, 19
Dirt tiles nr: 7, 12
Woods tiles nr: 6, 9, 14

crownField = 1
mine = 2
water = 3
Desert = 4
grassLand = 5
woodLand = 6
dirtLand = 7

"""