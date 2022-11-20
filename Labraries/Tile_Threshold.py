import cv2 as cv

def dominant_color_to_hsv(tile_colors):
    combined_tiles_HSV = cv.cvtColor(combined_tiles, cv.COLOR_BGR2HSV)




def tile_threshold(combined_tiles):

    #Converting image from BGR to HSV colorspace
    combined_tiles_HSV = cv.cvtColor(combined_tiles, cv.COLOR_BGR2HSV)

    #Hue er divideret med 2 er pga vi har fundet dem via paint.net, som viser hue fra 0-360, men CV2 vil hellere have det fra 0-180
    #Saturation og value er ganget med 2.55 pga paint.net viser fra 0-100 men cv2 vil gerne have det fra 0-255

    thresh_grass = cv.inRange(combined_tiles_HSV, (60/2, 65*2.55, 35.1*2.55), (95/2, 90*2.55, 70*2.55)) #Hue 0-180, Saturation 0-255, Value 0-255
    thresh_woods = cv.inRange(combined_tiles_HSV, (65/2, 40*2.55, 0*2.55), (90/2, 90*2.55, 35*2.55))
    thresh_water = cv.inRange(combined_tiles_HSV, (195/2, 45*2.55, 35*2.55), (220/2, 110*2.55, 80*2.55))
    thresh_desert = cv.inRange(combined_tiles_HSV, (40/2, 85*2.55, 50*2.55), (60/2, 105*2.55, 85*2.55))
    thresh_dirt = cv.inRange(combined_tiles_HSV, (40/2, 35*2.55, 30*2.55), (52/2, 59*2.55, 55*2.55))
    thresh_mine = cv.inRange(combined_tiles_HSV, (40/2, 48*2.55, 18*2.55), (50/2, 70*2.55, 29.9*2.55))

    cv.imshow("thresh_grass", thresh_grass)
    cv.imshow("thresh_woods", thresh_woods)
    cv.imshow("thresh_water", thresh_water)
    cv.imshow("thresh_desert", thresh_desert)
    cv.imshow("thresh_dirt", thresh_dirt)
    cv.imshow("thresh_mine", thresh_mine)

    #cv.waitKey(0)


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