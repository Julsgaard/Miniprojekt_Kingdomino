import cv2 as cv
import numpy as np
from Labraries import Non_Max_Suppression, Average_Tile_Color, Find_Crowns, Tile_Threshold, Connect_Tiles, Crown_Tile, \
    Count_Points, Remove_Start_Tile, Output_Image


# ------------------------------------------------- Loading the image -------------------------------------------------

# The image number from 1-74
image_number = 20

# Loading the image
image = cv.imread(f"King Domino dataset/Cropped and perspective corrected boards/{image_number}.jpg")


# -------------------------------------------- Finding the crowns positions --------------------------------------------

# Loading all crown templates from folder
templates = Find_Crowns.load_images_from_folder("Templates")

# Template matching and making bounding boxes around the crowns
crown_boxes = Find_Crowns.template_matching(image, templates)

# Runs the code if crowns have been found
if len(crown_boxes) != 0:
    # Non-max-suppression so the bounding boxes do not overlap
    crown_NMS_Boxes = Non_Max_Suppression.non_max_suppression(crown_boxes)

    # Getting the center coordinates of the bounding box
    crown_coordinates = Non_Max_Suppression.get_box_center(crown_NMS_Boxes)

    # Drawing the center coordinates on a black image
    crown_coordinates_image, crown_box_image = Non_Max_Suppression.draw_box_coordinates(image, crown_coordinates)

    # Converts the crown coordinates to a 5x5 numpy array
    crown_tile_matrix = Crown_Tile.find_crown_tile(image, crown_coordinates)

# Creating a default 5x5 numpy array if no crowns were found
else:
    crown_tile_matrix = np.zeros((5, 5))

# ---------------------------------------- Making tiles and getting thresholds ----------------------------------------

# Slices the image into 25 pieces
tiles = Average_Tile_Color.slice_img(image)

# Finds the median color of the tile and puts them into three lists of blue, green and red
blue_list, green_list, red_list = Average_Tile_Color.get_median_color(tiles)

# Combines the median colors into a 5x5 image
combined_tiles = Average_Tile_Color.set_tile_color(blue_list, green_list, red_list)

# Creates thresholds for each terrain type
thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine = \
    Tile_Threshold.tile_threshold(combined_tiles)


# ------------------------------------------ Finding the start tile position ------------------------------------------

# Loading all start tile templates from folder
start_tile_templates = Find_Crowns.load_images_from_folder("Start Tile Templates")

# Template matching and making bounding boxes around the start_tile
start_tile_boxes = Find_Crowns.template_matching(image, start_tile_templates)

# Runs the code if the start tile has been found
if len(start_tile_boxes) != 0:
    # Non-max-suppression so the bounding boxes do not overlap
    start_tile_NMS_Boxes = Non_Max_Suppression.non_max_suppression(start_tile_boxes)

    # Getting the center coordinates of the bounding box
    start_tile_box_center_coordinates = Non_Max_Suppression.get_box_center(start_tile_NMS_Boxes)

    # Drawing the center coordinates on a black image
    start_tile_coordinates_image, start_tile_box_image = \
        Non_Max_Suppression.draw_box_coordinates(image, start_tile_box_center_coordinates)

    # Converts the start_tile coordinates to a 5x5 numpy array
    start_tile_matrix = Crown_Tile.find_crown_tile(image, start_tile_box_center_coordinates)

    # Removes the start tile from the thresh images
    thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine = \
        Remove_Start_Tile.run_for_all_thresh \
            (start_tile_matrix, thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine)


# --------------------------------- Creating output image and calculating total points ---------------------------------

# Making an output image of all the tiles
output_image = Output_Image.output_image(thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt,
                                         thresh_mine)

# Running connect components for every threshold to find out if they are connected
connected_grass, connected_woods, connected_water, connected_desert, connected_dirt, connected_mine = \
    Connect_Tiles.connect_tile(thresh_grass, thresh_woods, thresh_water, thresh_desert, thresh_dirt, thresh_mine)

# Runs the code if crowns have been found
if len(crown_boxes) != 0:
    # Uses the crown tile matrix and the connected terrain types to calculate the total points
    total_points = Count_Points.connected_terrains \
        (crown_tile_matrix, connected_grass, connected_woods, connected_water, connected_desert, connected_dirt,
         connected_mine)

# Setting the total points to 0 if no crowns were found
else:
    total_points = 0


# ----------------------------------------------- Print and imshow data -----------------------------------------------

print(f"Crowns in tiles: \n {crown_tile_matrix}")
print(f"Total Points: {total_points}")

# cv.imshow("Grass threshold", thresh_grass)
# cv.imshow("Woods threshold", thresh_woods)
# cv.imshow("Water threshold", thresh_water)
# cv.imshow("Desert threshold", thresh_desert)
# cv.imshow("Dirt threshold", thresh_dirt)
# cv.imshow("Mine threshold", thresh_mine)

cv.imshow("Median tile color", combined_tiles)

try:
    cv.imshow("Start tile coordinates", start_tile_coordinates_image)
except:
    print("NO START TILE FOUND")

try:
    cv.imshow("Crown coordinates", crown_coordinates_image)
    cv.imshow("Crowns marked with boxes", crown_box_image)
except:
    print("NO CROWNS FOUND")

cv.imshow("Output image", output_image)

cv.waitKey(0)
