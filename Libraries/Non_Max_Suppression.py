import cv2
import numpy as np

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
    if len(boxes) == 0:
        return []

    newBoxes = np.zeros(boxes.shape)

    for i in range(len(boxes)):
        newBoxes[i, 0] = boxes[i, 2] - 11  # 11 is almost half of the template width
        newBoxes[i, 1] = boxes[i, 3] - 11  # 11 is almost half of the template height

    # Slicer så vi kun har 2 columns - 1 for x og 1 for y
    box_center_coordinates = newBoxes[:, :2]

    #Converts the value to an int and returns the value
    return box_center_coordinates.astype(int)


def draw_box_coordinates(image, boxes):
    if len(boxes) == 0:
        return [], []

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
        box_image = cv2.rectangle(new_image, (int(x[0]) + 14, int(x[1]) + 14), (int(x[0]) - 14, int(x[1]) - 14),
                                  (255, 255, 255), 2)

    return box_coordinates_image, box_image
