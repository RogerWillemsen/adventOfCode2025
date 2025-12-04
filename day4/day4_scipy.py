import numpy as np
import scipy as sc
import time

def perform_convolution(matrix, kernel):
    return sc.signal.convolve2d(matrix, kernel, mode='same')

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

number_rows = len(lines[0])
number_columns = len(lines)
can_access2 = 0
kernel = np.ones((3,3))

matrix = np.zeros((number_rows,number_columns))
for i in range(number_rows):
    for j in range(number_columns):
        if lines[i][j] == '@':
            matrix[i, j] = 1

# Part 1
result = perform_convolution(matrix, kernel)
can_access1 = np.sum((result < 5) * matrix)

# # Part 2
loop_counter = 0
while True:
    result = perform_convolution(matrix, kernel)
    new_access = np.sum((result < 5) * matrix)
    can_access2 += new_access
    matrix = (result >= 5) * matrix
    loop_counter += 1
    if new_access == 0:
        break

print("Can access part 1: %d" % can_access1)
print("Can access part 2: %d" % can_access2)
print("Number of iterations taken: %d" % loop_counter)
print("Time: %.6f" % (time.perf_counter() - start))