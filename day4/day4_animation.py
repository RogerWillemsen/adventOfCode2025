import numpy as np
import scipy as sc
import time
import os
import matplotlib.pyplot as plt
import matplotlib.colors as c
import matplotlib.animation as animation

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

animation_data = [matrix[:]]
loop_counter = 0
while True:
    result = perform_convolution(matrix, kernel)
    new_access = np.sum((result < 5) * matrix)
    can_access2 += new_access
    matrix = (result >= 5) * matrix
    animation_data.append(matrix[:])
    loop_counter += 1
    if new_access == 0:
        break

fig, ax = plt.subplots()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
cMap = c.ListedColormap(['red', 'limegreen'])
pcolor = ax.pcolormesh(animation_data[0], cmap=cMap)
ax.set_axis_off()

def update(frame):
    data = animation_data[frame]
    pcolor.set_array(data)
    return [pcolor]

ani = animation.FuncAnimation(fig=fig, func=update, frames=loop_counter, interval=120)
plt.show()
dir_path = os.path.dirname(os.path.realpath(__file__))
ani.save(filename=dir_path+"/output/animation.mp4", writer="ffmpeg")