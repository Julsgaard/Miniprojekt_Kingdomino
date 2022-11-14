import cv2
import Find_Crowns

image = cv2.imread("King Domino dataset/Cropped and perspective corrected boards/20.jpg")

cv2.imshow("image", image)


#Template matching and making bounding boxes around the crowns
boxes = Find_Crowns.template_matching(image)
#Non-max-suppression so the bounding boxes do not overlap
NMS_Boxes = Find_Crowns.non_max_suppression(boxes)
#Getting the center coordinates of the bounding box
box_center_coordinates = Find_Crowns.get_box_center(NMS_Boxes)
#Drawing the center coordinates on a black image
box_coordinates_image, box_image = Find_Crowns.draw_box_coordinates(image, box_center_coordinates)


print(f"Crowns in the image: {box_center_coordinates.shape[0]}")
print(f"Crown coordinates: \n {box_center_coordinates}")

cv2.imshow("image", image)
cv2.imshow("box_center_coordinates", box_coordinates_image)
cv2.imshow("box_image", box_image)
cv2.waitKey(0)
