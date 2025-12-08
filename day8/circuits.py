import numpy as np
import math
import networkx as nx

# with open("day8/box_map_test.txt") as f:
#     rows = f.read().splitlines()

with open("day8/box_map.txt") as f:
    rows = f.read().splitlines()

box_coordinates = np.array([r.split(",") for r in rows]).astype(int)
print(box_coordinates)

def cartesian_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

distance_matrix = np.zeros((len(box_coordinates), len(box_coordinates)))
for i, box in enumerate(box_coordinates):
    for j, other_box in enumerate(box_coordinates):
        if i == j:
            distance_matrix[i, j] = 0
            continue
        else:
            distance = cartesian_distance(box, other_box)
            distance_matrix[i, j] = distance
# print(distance_matrix)
tri_rows, tri_cols = np.triu_indices_from(distance_matrix, k=1)
extracted_distances = distance_matrix[tri_rows, tri_cols]

distance_index_pairs = []
for i in range(len(extracted_distances)):
    distance_index_pairs.append([extracted_distances[i], (tri_rows[i], tri_cols[i])])
distance_index_pairs.sort(key=lambda x: x[0])
# print(distance_index_pairs)

G = nx.Graph()
G.add_nodes_from(range(len(box_coordinates)))

# PART 1
# TARGET_CONNECTIONS = 10
TARGET_CONNECTIONS = 1000

for connection in range(TARGET_CONNECTIONS):
    boxes = distance_index_pairs[connection][1]
    G.add_edge(boxes[0], boxes[1])

components = list(nx.connected_components(G))
group_sizes = [len(c) for c in components]
for i, component_indices in enumerate(components):
    group_coords = [box_coordinates[idx] for idx in component_indices]
    print(f"Group {i+1}: Contains {len(group_coords)} coordinates.")
    # print(f"  Coordinates: {group_coords}")
group_sizes.sort(reverse=True)
print(math.prod(group_sizes[:3]))

# PART 2
num_groups = len(box_coordinates)
connection = 0
while num_groups >= 2:
    boxes = distance_index_pairs[connection][1]
    G.add_edge(boxes[0], boxes[1])
    num_groups = len(list(nx.connected_components(G)))
    connection += 1

connection -= 1  # Step back to the last valid connection
print("Total connections made:", connection + 1)
components = list(nx.connected_components(G))

print("Final connection:", distance_index_pairs[connection])
idx_1 = distance_index_pairs[connection][1][0]
idx_2 = distance_index_pairs[connection][1][1]
print("Boxes:", box_coordinates[idx_1], box_coordinates[idx_2])
print("Extensions cable (prod of x):", box_coordinates[idx_1][0] * box_coordinates[idx_2][0])