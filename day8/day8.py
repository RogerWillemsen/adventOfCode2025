import time
import numpy as np
from scipy.spatial.distance import cdist

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

n_points = len(lines)
n_connections = 1000
junctions = np.zeros((n_points, 3))
for i, line in enumerate(lines):
    junctions[i,:] = [int(val) for val in line.split(',')]

distances = np.triu(cdist(junctions, junctions))
distances[distances == 0] = None

closest_junctions = np.unravel_index(np.argsort(distances.ravel()), distances.shape)

three_largest = 0
last_two = 0
circuits = []
connected = set()
for i, (j1, j2) in enumerate(zip(closest_junctions[0], closest_junctions[1])):
    connected.add(j1)
    connected.add(j2)
    last_connected = None
    for circuit in circuits:
        if j1 in circuit or j2 in circuit:
            if last_connected is not None:
                circuit.update(last_connected)
                circuits.remove(last_connected)
            last_connected = circuit
            circuit.add(j1)
            circuit.add(j2)
    if last_connected is None:
        circuits.append({j1, j2})
    if len(connected) == n_points:
        last_two = junctions[j1,0] * junctions[j2,0]
        break
    if i == n_connections - 1:
        circuit_sizes = [len(circuit) for circuit in circuits]
        three_largest = np.prod(np.sort(circuit_sizes)[-3:])

print("Product of three largest circuits: %d" % three_largest)
print("Product of last two junctions: %d" % last_two)
print("Time: %.6f" % (time.perf_counter() - start))
