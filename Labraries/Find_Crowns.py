import numpy as np
import cv2


#TODO: Make a template list with more templates so the template matching is more accurate

template_up = cv2.imread('Templates/Crown_up.png')
template_down = cv2.imread('Templates/Crown_down.png')
template_right = cv2.imread('Templates/Crown_right.png')
template_left = cv2.imread('Templates/Crown_left.png')

def template_matching(image):
    template_match_up = cv2.matchTemplate(image, template_up, cv2.TM_CCOEFF_NORMED)
    template_match_down = cv2.matchTemplate(image, template_down, cv2.TM_CCOEFF_NORMED)
    template_match_right = cv2.matchTemplate(image, template_right, cv2.TM_CCOEFF_NORMED)
    template_match_left = cv2.matchTemplate(image, template_left, cv2.TM_CCOEFF_NORMED)

    ret, output_up = cv2.threshold(template_match_up, 0.6, 1, cv2.THRESH_BINARY)
    ret, output_down = cv2.threshold(template_match_down, 0.6, 1, cv2.THRESH_BINARY)
    ret, output_right = cv2.threshold(template_match_right, 0.6, 1, cv2.THRESH_BINARY)
    ret, output_left = cv2.threshold(template_match_left, 0.5, 1, cv2.THRESH_BINARY)

    output1 = output_up + output_down
    output2 = output_right + output_left

    (template_up_down_width, template_up_down_height) = template_up.shape[:2]
    template_up_down_width = int(template_up_down_width / 2)
    template_up_down_height = int(template_up_down_height / 2)

    (template_left_right_width, template_left_right_height) = template_up.shape[:2]
    template_left_right_width = int(template_left_right_width / 2)
    template_left_right_height = int(template_left_right_height / 2)

    constant_up_down = cv2.copyMakeBorder(output1, template_up_down_width, template_up_down_width - 1,
                                          template_up_down_height, template_up_down_height,
                                          cv2.BORDER_CONSTANT, value=[0, 0, 0])

    constant_left_right = cv2.copyMakeBorder(output2, template_left_right_height, template_left_right_height,
                                             template_left_right_width,
                                             template_left_right_width - 1, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    output = constant_up_down + constant_left_right

    (y1, x1) = np.where(output >= 0.45)  # object is detected, where the correlation is above the treshold
    boxes = np.zeros((len(y1), 4))  # construct array of zeros
    x2 = x1 + template_left_right_height  # calculate x2 with the width of the template
    y2 = y1 + template_up_down_height  # calculate y2 with the height of the template
    # fill the bounding boxes array
    boxes[:, 0] = x1
    boxes[:, 1] = y1
    boxes[:, 2] = x2
    boxes[:, 3] = y2

    return boxes.astype(int)


