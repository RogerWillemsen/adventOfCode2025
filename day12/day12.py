import time

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

goals = []
shape_sizes = []
shape_size = 0
shape_start = None
for i,line in enumerate(lines):
    if len(line) == 0 and shape_start is not None:
        shape_start = None
        shape_sizes.append(shape_size)
    elif line[-1] == ':':
        shape_start = i
        shape_size = 0
    elif shape_start is not None:
        shape_size += sum([1 if c == '#' else 0 for c in line])
    else:
        parts = line.split(": ")
        region = (int(parts[0].split("x")[0]), int(parts[0].split("x")[1]))
        goal = [int(p) for p in parts[1].split(" ")]
        goals.append((region, goal))

count_fit = 0
count_maybe = 0
for region, goal in goals:
    size = region[0] * region[1]
    number_shapes = sum(goal)
    if number_shapes * 9 <= size:
        count_fit += 1
    elif sum([shape_sizes[i] * g for i,g in enumerate(goal)]) <= size:
        count_maybe += 1

if count_maybe == 0:
    print("Number of regions: %d" % count_fit)
else:
    print("Could not determine")
print("Time: %.6f" % (time.perf_counter() - start))








