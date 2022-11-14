import numpy as np
import cv2


#TODO: Make a template list with more templates so the template matching is more accurate

template_up = cv2.imread("Crown_up.png")
template_down = cv2.imread("Crown_down.png")
template_right = cv2.imread("Crown_right.png")
template_left = cv2.imread("Crown_left.png")


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


def non_max_suppression(boxes, probs=None, overlapThresh=0.3):
    # if there are no boxes, return an empty list
    if len(boxes) == 0:
        return []

    # if the bounding boxes are integers, convert them to floats -- this
    # is important since we'll be doing a bunch of divisions
    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    # initialize the list of picked indexes
    pick = []

    # grab the coordinates of the bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    # compute the area of the bounding boxes and grab the indexes to sort
    # (in the case that no probabilities are provided, simply sort on the
    # bottom-left y-coordinate)
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = y2

    # if probabilities are provided, sort on them instead
    if probs is not None:
        idxs = probs

    # sort the indexes
    idxs = np.argsort(idxs)

    # keep looping while some indexes still remain in the indexes list
    while len(idxs) > 0:
        # grab the last index in the indexes list and add the index value
        # to the list of picked indexes
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        # find the largest (x, y) coordinates for the start of the bounding
        # box and the smallest (x, y) coordinates for the end of the bounding
        # box
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        # compute the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        # compute the ratio of overlap
        overlap = (w * h) / area[idxs[:last]]

        # delete all indexes from the index list that have overlap greater
        # than the provided overlap threshold
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))

    # return only the bounding boxes that were picked
    return boxes[pick].astype("int")


def get_box_center(boxes):
    newBoxes = np.zeros(boxes.shape)

    for i in range(len(boxes)):
        newBoxes[i, 0] = boxes[i, 2] - 6.5  # 13 er template width, så ved at minus med halvdelen får vi centret
        newBoxes[i, 1] = boxes[i, 3] - 6.5  # 13 er også template height, så her minuser vi også med halvdelen

    # Slicer så vi kun har 2 columns - 1 for x og 1 for y
    newBoxes = newBoxes[:, :2]
    # print(newBoxes)

    # newBoxes[i, 0] = np.maximum(boxes[i, 0], boxes[i, 2])
    # newBoxes[i, 2] = np.minimum(boxes[i, 0], boxes[i, 2])
    # newBoxes[i, 0] = newBoxes[i, 0] - newBoxes[i, 2]
    return newBoxes


def draw_box_coordinates(image, boxes):
    #Making a numpy array with zeros, same size as the image
    box_coordinates_image = np.zeros(image.shape)
    # print(boxes.shape)

    # So the rectangle is not saved on the original image - Makes a copy of the image
    new_image = image.copy()

    for x in boxes:
        # print(f"x:{x}")
        #Draw white dots on black image
        box_coordinates_image[int(x[1]), int(x[0])] = 1

        #Draw boxes on image
        box_image = cv2.rectangle(new_image, (int(x[0]) - 20, int(x[1]) - 20), (int(x[0]) + 8, int(x[1]) + 8),
                                  (255, 255, 255), 2)

    return box_coordinates_image, box_image


def draw_box_img(img, boxes):
    for x in boxes:
        # print(f"x:{x}")
        box_image = cv2.rectangle(img, (int(x[0]) + 13, int(x[1]) + 13), (int(x[0]) - 13, int(x[1]) - 13), (0, 255, 0),
                                  3)

    return box_image
