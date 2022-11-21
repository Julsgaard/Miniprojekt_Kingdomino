import cv2

from Labraries import Non_Max_Suppression, Average_Tile_Color, Find_Crowns, Tile_Threshold, Connect_Tiles, Crown_Tile, \
    Count_Points

image = cv2.imread("King Domino dataset/Cropped and perspective corrected boards/20.jpg")

# Template matching and making bounding boxes around the crowns
boxes = Find_Crowns.template_matching(image)

# Non-max-suppression so the bounding boxes do not overlap
NMS_Boxes = Non_Max_Suppression.non_max_suppression(boxes)

# Getting the center coordinates of the bounding box
box_center_coordinates = Non_Max_Suppression.get_box_center(NMS_Boxes)

# Drawing the center coordinates on a black image
box_coordinates_image, box_image = Non_Max_Suppression.draw_box_coordinates(image, box_center_coordinates)

# Converts the crown coordinates to a 5x5 numpy array
crown_tile = Crown_Tile.find_crown_tile(box_center_coordinates, image.shape[0], image.shape[1])

#Slices the image into 25 pieces
tiles = Average_Tile_Color.slice_img(image)

#AVERAGE OR MEDIAN ONLY RUN ONE
#blue_list, green_list, red_list = Average_Tile_Color.get_average_color(tiles)
blue_list, green_list, red_list = Average_Tile_Color.get_median_color(tiles)


combined_tiles = Average_Tile_Color.set_tile_color(blue_list, green_list, red_list)

thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine = \
    Tile_Threshold.tile_threshold(combined_tiles)

connected_grass, connected_woods, connected_water, connected_desert, connected_dirt, connected_mine = \
    Connect_Tiles.connect_tile(thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine)

total_points = Count_Points.connected_terrains \
    (crown_tile, connected_grass, connected_woods, connected_water, connected_desert, connected_dirt, connected_mine)


print(f"Crown tiles: \n {crown_tile}")
print(f"Total Points: {total_points}")

cv2.imshow("combined tiles", combined_tiles)
# cv2.imshow("tiles_dominant_color", tiles_dominant_color)
# cv2.imshow("tile", tiles[0][0])
# cv2.imshow("average_color", tiles_average_color[])
#cv2.imshow("image", image)
# cv2.imshow("box_center_coordinates", box_coordinates_image)
cv2.imshow("box_image", box_image)
cv2.waitKey(0)
