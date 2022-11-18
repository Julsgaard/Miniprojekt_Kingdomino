import cv2

import Average_Tile_Color
import Crown_Tile
import Find_Crowns
import Non_Max_Suppression

image = cv2.imread("King Domino dataset/Cropped and perspective corrected boards/20.jpg")


#Template matching and making bounding boxes around the crowns
boxes = Find_Crowns.template_matching(image)

#Non-max-suppression so the bounding boxes do not overlap
NMS_Boxes = Non_Max_Suppression.non_max_suppression(boxes)

#Getting the center coordinates of the bounding box
box_center_coordinates = Non_Max_Suppression.get_box_center(NMS_Boxes)

#Drawing the center coordinates on a black image
box_coordinates_image, box_image = Non_Max_Suppression.draw_box_coordinates(image, box_center_coordinates)

#TODO: Få de tiles der er kroner på
#crown_tile = Crown_Tile.find_crown_tile(box_center_coordinates, image.shape[0], image.shape[1])

# print(f"Crowns in the image: {box_center_coordinates.shape[0]}")
# print(f"Crown coordinates: \n {box_center_coordinates}")
# print(f"Crown Tiles: \n {crown_tile}")


tiles = Average_Tile_Color.slice_IMG(image)

tiles_dominant_color = Average_Tile_Color.get_dominant_colour(tiles)

combined_tiles = Average_Tile_Color.set_tile_color(tiles_dominant_color)

cv2.imshow("combined tiles", combined_tiles)
#cv2.imshow("average_color", tiles_average_color[])
cv2.imshow("image", image)
cv2.imshow("box_center_coordinates", box_coordinates_image)
cv2.imshow("box_image", box_image)
cv2.waitKey(0)
