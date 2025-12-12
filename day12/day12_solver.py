import time
import numpy as np
import scipy.optimize as optimize

with open('example.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

shapes = []
goals = []
shape_start = None
shape = None
for i,line in enumerate(lines):
    if len(line) == 0 and shape_start is not None:
        shape_start = None
        shapes.append(shape.copy())
    elif line[-1] == ':':
        shape_start = i
        shape = np.zeros((3,3))
    elif shape_start is not None:
        shape[i-shape_start-1] = [1 if c == '#' else 0 for c in line]
    else:
        parts = line.split(": ")
        region = (int(parts[0].split("x")[0]), int(parts[0].split("x")[1]))
        goal = [int(p) for p in parts[1].split(" ")]
        goals.append((region, goal))

shape_options = {}
for i,shape in enumerate(shapes):
    rot90 = np.array(list(zip(*shape[::-1])))
    rot180 = np.array(list(zip(*rot90[::-1])))
    rot270 = np.array(list(zip(*rot180[::-1])))
    mirror = shape[:,::-1]
    mirror90 = np.array(list(zip(*mirror[::-1])))
    mirror180 = np.array(list(zip(*mirror90[::-1])))
    mirror270 = np.array(list(zip(*mirror180[::-1])))
    options = [shape, rot90, rot180, rot270, mirror, mirror90, mirror180, mirror270]
    shape_options[i] = [s1 for i, s1 in enumerate(options) if not any(((s1 == s2).all() for s2 in options[:i]))]

def create_grid_options(original_grid, shape):
    region = original_grid.shape
    options = []
    for i in range(region[0]-2):
        for j in range(region[1]-2):
            new_grid = np.zeros(region)
            new_grid[i:i+3,j:j+3] = shape
            options.append(new_grid)
    return options

count = 0
for region, goal in goals:
    grid = np.zeros(region)
    all_possible_pos = {}
    for i in shape_options:
        shapes = shape_options[i]
        possible_pos = []
        for shape in shapes:
            possible_pos += create_grid_options(grid, shape)
        all_possible_pos[i] = possible_pos

    n_shape = len(all_possible_pos)
    n_grid = len(grid.flatten())
    n_pos = sum([len(i) for i in all_possible_pos.values()])
    A_ub = np.zeros((n_grid, n_pos))
    A_eq = np.zeros((n_shape, n_pos))
    b_ub = [1] * n_grid
    b_eq = goal
    bounds = [(0,1)] * n_pos
    c = [1] * n_pos

    i = 0
    for shape_i in all_possible_pos:
        for const_i, pos_shape in enumerate(all_possible_pos[shape_i]):
            A_ub[0:n_grid,i] = pos_shape.reshape((1, n_grid))
            A_eq[shape_i, i] = 1
            i += 1

    res = optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=1)
    if res.success:
        count += 1

    print('Solved for:', region, goal)
    print('Current count: %d' % count)
    print("Time: %.6f" % (time.perf_counter() - start))
    start = time.perf_counter()
