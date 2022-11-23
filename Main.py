import cv2 as cv
import numpy as np
from Labraries import Non_Max_Suppression, Average_Tile_Color, Find_Crowns, Tile_Threshold, Connect_Tiles, Crown_Tile, \
    Count_Points, Remove_Start_Tile, Output_Image

# Loading test image
image = cv.imread("King Domino dataset/Cropped and perspective corrected boards/46.jpg")

# Loading all images from folder
# images = Find_Crowns.load_images_from_folder("King Domino dataset/Cropped and perspective corrected boards/")



# Loading all crown templates from folder
templates = Find_Crowns.load_images_from_folder("Templates")

# Template matching and making bounding boxes around the crowns
boxes = Find_Crowns.template_matching(image, templates)

# Cron_tile = 0 if no Crowns were found
if len(boxes) != 0:
    # Non-max-suppression so the bounding boxes do not overlap
    NMS_Boxes = Non_Max_Suppression.non_max_suppression(boxes)

    # Getting the center coordinates of the bounding box
    box_center_coordinates = Non_Max_Suppression.get_box_center(NMS_Boxes)

    # Drawing the center coordinates on a black image
    box_coordinates_image, box_image = Non_Max_Suppression.draw_box_coordinates(image, box_center_coordinates)

    # Converts the crown coordinates to a 5x5 numpy array
    crown_tile = Crown_Tile.find_crown_tile(box_center_coordinates, image.shape[0], image.shape[1])

else:
    crown_tile = np.zeros((5, 5))


# Slices the image into 25 pieces
tiles = Average_Tile_Color.slice_img(image)

# AVERAGE OR MEDIAN TILE COLOR ***ONLY RUN ONE***
# blue_list, green_list, red_list = Average_Tile_Color.get_average_color(tiles)
blue_list, green_list, red_list = Average_Tile_Color.get_median_color(tiles)

combined_tiles = Average_Tile_Color.set_tile_color(blue_list, green_list, red_list)

thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine = \
    Tile_Threshold.tile_threshold(combined_tiles)



# Loading all start tile templates from folder
start_tile_templates = Find_Crowns.load_images_from_folder("Start Tile Templates")

# Template matching and making bounding boxes around the start_tile
start_tile_boxes = Find_Crowns.template_matching(image, start_tile_templates)

if len(start_tile_boxes) != 0:
    # Non-max-suppression so the bounding boxes do not overlap
    start_tile_NMS_Boxes = Non_Max_Suppression.non_max_suppression(start_tile_boxes)

    # Getting the center coordinates of the bounding box
    start_tile_box_center_coordinates = Non_Max_Suppression.get_box_center(start_tile_NMS_Boxes)

    # Drawing the center coordinates on a black image
    start_tile_box_coordinates_image, start_tile_box_image = \
        Non_Max_Suppression.draw_box_coordinates(image, start_tile_box_center_coordinates)

    # Converts the start_tile coordinates to a 5x5 numpy array
    start_tile = Crown_Tile.find_crown_tile(start_tile_box_center_coordinates, image.shape[0], image.shape[1])

    # Removes the start tile from the thresh images
    thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine = \
        Remove_Start_Tile.run_for_all_thresh \
            (start_tile, thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine)



# Making an output image of all the tiles
output_image = Output_Image.output_image(thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt,
                                         thresh_mine)

# Running connect components for every threshold
connected_grass, connected_woods, connected_water, connected_desert, connected_dirt, connected_mine = \
    Connect_Tiles.connect_tile(thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine)

# Calculates the total points
if len(boxes) != 0:
    total_points = Count_Points.connected_terrains \
        (crown_tile, connected_grass, connected_woods, connected_water, connected_desert, connected_dirt,
         connected_mine)
else:
    total_points = 0



print(f"Crown tiles: \n {crown_tile}")
print(f"Total Points: {total_points}")


cv.imshow("thresh_grass", thresh_grass)
cv.imshow("thresh_woods", thresh_woods)
cv.imshow("thresh_water", thresh_water)
cv.imshow("thresh_desert", thresh_desert)
cv.imshow("thresh_dirt", thresh_dirt)
cv.imshow("thresh_mine", thresh_mine)

cv.imshow("combined tiles", combined_tiles)

# cv2.imshow("tiles_dominant_color", tiles_dominant_color)
# cv2.imshow("tile", tiles[0][0])
# cv2.imshow("average_color", tiles_average_color[])
# cv2.imshow("image", image)

try:
    cv.imshow("start_tile_box_center_coordinates", start_tile_box_coordinates_image)
except:
    print("NO START TILE FOUND")

try:
    cv.imshow("box_center_coordinates", box_coordinates_image)
    cv.imshow("box_image", box_image)
except:
    print("NO CROWNS FOUND")

cv.imshow("Output_Image", output_image)


cv.waitKey(0)
