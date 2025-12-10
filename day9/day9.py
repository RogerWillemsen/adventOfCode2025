import time
import itertools as it
import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

tiles = np.zeros((len(lines), 2))
tiles_index = range(len(lines))
for i,line in enumerate(lines):
    tiles[i] = [int(val) for val in line.split(',')]

combinations = list(it.combinations(tiles_index, 2))

area = []
for combination in combinations:
    area.append((abs(tiles[combination[0]][0] - tiles[combination[1]][0]) + 1) * (abs(tiles[combination[0]][1] - tiles[combination[1]][1]) + 1))

print("Largest area part 1: %d" % max(area))
print("Time: %.6f" % (time.perf_counter() - start))

area_sorted = np.argsort(area)[::-1]
sorted_combinations = np.array(combinations)[area_sorted]
lines = np.append(tiles, [tiles[0]], axis=0)
tile_pairs = it.pairwise(lines)
max_area_index = None
for i,combination in enumerate(sorted_combinations):
    tiles_rect = tiles[combination]
    min_x = np.min(tiles_rect[:, 0])
    max_x = np.max(tiles_rect[:, 0])
    min_y = np.min(tiles_rect[:, 1])
    max_y = np.max(tiles_rect[:, 1])

    line_inside_rect = False
    for tile1, tile2 in it.pairwise(lines):
        if (max(tile1[0], tile2[0]) > min_x and max_x > min(tile1[0], tile2[0]) and
                max(tile1[1], tile2[1]) > min_y and max_y > min(tile1[1], tile2[1])):
            line_inside_rect = True
            break

    if not line_inside_rect:
        max_area_index = i
        break

max_area = np.array(area)[area_sorted][max_area_index]
print("Largest area part 2: %d" % max_area)
print("Time: %.6f" % (time.perf_counter() - start))



