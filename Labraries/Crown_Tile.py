import numpy as np


def find_crown_tile(image, center_coordinates):
    if len(center_coordinates) == 0:
        return np.zeros((5, 5))

    crown_tile_matrix = np.zeros((5, 5))

    image_shape_x, image_shape_y = image.shape[0], image.shape[1]

    # The pixel length between each tile when there are 5x5 tiles
    tile_pixel_length_x = image_shape_x / 5
    tile_pixel_length_y = image_shape_y / 5

    # Loop goes through every crown coordinate
    for i in range(len(center_coordinates)):
        crown_tile_x = center_coordinates[i][0] / tile_pixel_length_x
        crown_tile_y = center_coordinates[i][1] / tile_pixel_length_y

        crown_tile_x = int(crown_tile_x)
        crown_tile_y = int(crown_tile_y)

        crown_tile_matrix[crown_tile_y][crown_tile_x] += 1

    return crown_tile_matrix
