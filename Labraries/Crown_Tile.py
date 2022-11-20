import numpy as np

def find_crown_tile(box_coordinates_image, image_shape_x, image_shape_y):
    crown_tile = np.zeros(box_coordinates_image.shape)

    for i in range(len(box_coordinates_image)):
        box_tile_x = image_shape_x / box_coordinates_image[i][0]
        box_tile_y = image_shape_y / box_coordinates_image[i][1]

        crown_tile[i, 0] = box_tile_x
        crown_tile[i, 1] = box_tile_y

    #crown_tile = crown_tile.astype(int)

    print(f"Tile: \n {crown_tile}")

    #return crown_tile