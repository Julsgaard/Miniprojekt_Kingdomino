import numpy as np


def slice_img(img):
    img_width, img_height = img.shape[0], img.shape[1]
    slice_width, slice_height = img_width / 5, img_height / 5
    width, height = int(slice_width), int(slice_height)

    slice_list = []

    for y in range(5):
        for x in range(5):
            slice = img[width * y: width * (y + 1), height * x:height * (x + 1)]
            slice_list.append(slice)

    return slice_list


def get_average_color(tile_colors):
    blue_list = []
    red_list = []
    green_list = []
    for i in range(len(tile_colors)):
        width, height = tile_colors[i].shape[0], tile_colors[i].shape[1]

        blue, green, red = 0, 0, 0

        for x in range(width):
            for y in range(height):
                # print(f"{x},{y}")
                blue += tile_colors[i][x, y, 0]
                green += tile_colors[i][x, y, 1]
                red += tile_colors[i][x, y, 2]

        # Calculates the average color
        blue /= width * height
        green /= width * height
        red /= width * height

        blue_list.append(blue)
        green_list.append(green)
        red_list.append(red)

    return blue_list, green_list, red_list

def get_median_color(tile_colors):
    blue_median_list = []
    green_median_list = []
    red_median_list = []

    for i in range(len(tile_colors)):
        blue_list = []
        green_list = []
        red_list = []

        width, height = tile_colors[i].shape[0], tile_colors[i].shape[1]

        for x in range(width):
            for y in range(height):
                # print(f"{x},{y}")
                blue = tile_colors[i][x, y, 0]
                green = tile_colors[i][x, y, 1]
                red = tile_colors[i][x, y, 2]

                blue_list.append(blue)
                green_list.append(green)
                red_list.append(red)

        blue_list.sort()
        green_list.sort()
        red_list.sort()

        blue_median = np.median(blue_list)
        green_median = np.median(green_list)
        red_median = np.median(red_list)

        blue_median_list.append(blue_median)
        green_median_list.append(green_median)
        red_median_list.append(red_median)

    print(f"blue_median LIST: {blue_median_list}")

    return blue_median_list, green_median_list, red_median_list


def set_tile_color(blue_list, green_list, red_list):
    matrix = np.zeros((25, 1, 3), dtype=np.uint8)

    for i in range(len(matrix)):
        matrix[i, 0, 0] = blue_list[i]
        matrix[i, 0, 1] = green_list[i]
        matrix[i, 0, 2] = red_list[i]

    matrix_2d = np.reshape(matrix, (5, 5, 3))

    return matrix_2d
