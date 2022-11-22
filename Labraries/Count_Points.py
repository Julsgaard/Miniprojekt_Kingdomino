import numpy as np


def connected_terrains(crown_tile, connected_grass, connected_woods, connected_water,
                       connected_desert, connected_dirt, connected_mine):
    def count_points(connected_terrain_type):
        figures_amount = np.max(connected_terrain_type)

        if figures_amount == 0:
            return 0

        points = 0

        for i in range(figures_amount):
            connected_tiles_amount = 0
            tile_position_x = []
            tile_position_y = []
            crowns = 0
            for y in range(len(connected_terrain_type[:, 0])):
                for x in range(len(connected_terrain_type[0, :])):
                    if connected_terrain_type[y, x] == i + 1:
                        connected_tiles_amount += 1
                        tile_position_y.append(y)
                        tile_position_x.append(x)
            for i in range(connected_tiles_amount):
                crowns += crown_tile[tile_position_y[i], tile_position_x[i]]
            points += connected_tiles_amount * crowns

        # print(f"tile_position_y: {tile_position_y}")
        # print(f"tile_position_x: {tile_position_x}")
        # print(f"crowns: {crowns}")

        return points
    points_grass = count_points(connected_grass)
    points_woods = count_points(connected_woods)
    points_water = count_points(connected_water)
    points_desert = count_points(connected_desert)
    points_dirt = count_points(connected_dirt)
    points_mine = count_points(connected_mine)

    print(f"points_grass: {points_grass}")
    print(f"points_woods: {points_woods}")
    print(f"points_water: {points_water}")
    print(f"points_desert: {points_desert}")
    print(f"points_dirt: {points_dirt}")
    print(f"points_mine: {points_mine}")

    total_points = points_grass + points_woods + points_water + points_desert + points_dirt + points_mine

    return total_points
