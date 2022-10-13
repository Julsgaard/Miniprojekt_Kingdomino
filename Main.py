import cv2
import numpy as np

image = cv2.imread("20.jpg")
template_up = cv2.imread("Crown_up.png")
template_down = cv2.imread("Crown_down.png")
template_right = cv2.imread("Crown_right.png")
template_left = cv2.imread("Crown_left.png")


matchTemplate_up = cv2.matchTemplate(image, template_up, cv2.TM_CCOEFF_NORMED)
matchTemplate_down = cv2.matchTemplate(image, template_down, cv2.TM_CCOEFF_NORMED)
matchTemplate_right = cv2.matchTemplate(image, template_right, cv2.TM_CCOEFF_NORMED)
matchTemplate_left = cv2.matchTemplate(image, template_left, cv2.TM_CCOEFF_NORMED)


ret, output_up = cv2.threshold(matchTemplate_up, 0.6, 1, cv2.THRESH_BINARY)
ret, output_down = cv2.threshold(matchTemplate_down, 0.6, 1, cv2.THRESH_BINARY)
ret, output_right = cv2.threshold(matchTemplate_right, 0.6, 1, cv2.THRESH_BINARY)
ret, output_left = cv2.threshold(matchTemplate_left, 0.5, 1, cv2.THRESH_BINARY)


output1 = output_up + output_down
output2 = output_right + output_left
#output = output1 + output2


size_updown_x = template_up.shape[1]/2
size_updown_x = int(size_updown_x)
size_updown_y = template_up.shape[0]/2
size_updown_y = int(size_updown_y)

print("size x:", int(size_updown_x))
print("size y:", size_updown_y)

#BLUE = [255,0,0]
constant_updown = cv2.copyMakeBorder(output1, size_updown_y,size_updown_y-1,size_updown_x,size_updown_x,
                                     cv2.BORDER_CONSTANT, value=[0,0,0])

size_leftright_x = template_right.shape[1]/2
size_leftright_x = int(size_updown_x)
size_leftright_y = template_right.shape[0]/2
size_leftright_y = int(size_updown_y)

constant_leftright = cv2.copyMakeBorder(output2, size_leftright_x,size_leftright_x,size_leftright_y,size_leftright_y-1,
                                        cv2.BORDER_CONSTANT, value=[0,0,0])

output = constant_updown + constant_leftright

#number_of_white_pix = np.sum(output == 255)

#print('Number of white pixels:', number_of_white_pix)

cv2.imshow("Input", image)
#cv2.imshow("Constant updown", constant_updown)
#cv2.imshow("Constant leftright", constant_leftright)
cv2.imshow("Output", output)

cv2.waitKey(0)
