import numpy as np
import cv2 as cv
import os


# Loads images from a folder and assigns them to the list templates
def load_images_from_folder(folder):
    # Creating the list
    templates = []
    # Goes through all files in the folder
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder, filename))
        if img is not None:
            templates.append(img)
    return templates

# Used for template matching
def template_matching(image, templates):
    constant_list = []

    for i in range(len(templates)):
        template = cv.matchTemplate(image, templates[i], cv.TM_CCOEFF_NORMED)

        ret, threshold = cv.threshold(template, 0.56, 1, cv.THRESH_BINARY)

        template_width, template_height = templates[i].shape[:2]

        template_width = template_width / 2
        template_height = template_height / 2

        template_width_int = int(template_width)
        template_height_int = int(template_height)

        # To get a 500x500 array - The template can be any pixel size fx. (24,25), (25,24), (24,24) or (25,25)
        if template_width.is_integer() and not template_height.is_integer():
            constant = cv.copyMakeBorder(threshold, template_width_int, template_width_int - 1, template_height_int,
                                         template_height_int, cv.BORDER_CONSTANT, value=[0, 0, 0])

        elif template_height.is_integer() and not template_width.is_integer():
            constant = cv.copyMakeBorder(threshold, template_width_int, template_width_int, template_height_int,
                                         template_height_int - 1, cv.BORDER_CONSTANT, value=[0, 0, 0])

        elif template_height.is_integer() and template_width.is_integer():
            constant = cv.copyMakeBorder(threshold, template_width_int, template_width_int - 1, template_height_int,
                                         template_height_int - 1, cv.BORDER_CONSTANT, value=[0, 0, 0])
        else:
            constant = cv.copyMakeBorder(threshold, template_width_int, template_width_int, template_height_int,
                                         template_height_int, cv.BORDER_CONSTANT, value=[0, 0, 0])

        # For testing
        # print(constant.shape)
        # print(template_width, template_height)
        # cv.imshow("threshold", threshold)
        # cv.imshow("template", template)
        # cv.waitKey(0)

        constant_list.append(constant)

    constants = 0
    for i in range(len(constant_list)):
        constants += constant_list[i]

    (y1, x1) = np.where(constants >= 0.45)  # object is detected, where the correlation is above the treshold

    boxes = np.zeros((len(y1), 4))  # construct array of zeros

    x2 = x1 + 12
    y2 = y1 + 12

    # fill the bounding boxes array
    boxes[:, 0] = x1
    boxes[:, 1] = y1
    boxes[:, 2] = x2
    boxes[:, 3] = y2

    return boxes.astype(int)
