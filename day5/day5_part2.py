import numpy as np
import time

with open('input.txt') as f:
    lines = f.read().splitlines()

# Read data
ranges = []
for line in lines:
    if '-' in line:
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
    elif len(line) == 0:
        break

# Prepare data
ranges = np.array(ranges)

start = time.perf_counter()

# Sort
order = np.argsort(ranges[:, 0])
ranges = ranges[order]

count = 0
range_start = 0
range_end = 0
for i in range(len(ranges)):
    if ranges[i, 1] <= range_end:
        continue
    if ranges[i, 0] <= range_end:
        range_start = range_end + 1
    else:
        range_start = ranges[i, 0]
    range_end = ranges[i, 1]
    count += range_end - range_start + 1

print("Total number of fresh ingredient ids: %d" % count)
print("Time: %.6f" % (time.perf_counter() - start))