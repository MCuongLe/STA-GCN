import sys
import numpy as np

sys.path.extend(['../'])
from graph import tools

num_node = 25
self_link = [(i, i) for i in range(num_node)]
inward_ori_index = [(1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6),
                    (8, 7), (9, 21), (10, 9), (11, 10), (12, 11), (13, 1),
                    (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18),
                    (20, 19), (22, 23), (23, 8), (24, 25), (25, 12)]
inward = [(i - 1, j - 1) for (i, j) in inward_ori_index]
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward


class Graph:
    def __init__(self, *args, **kwargs):
        self.edges = neighbor
        self.num_nodes = num_node
        self.self_loops = [(i, i) for i in range(self.num_nodes)]
        self.A_binary = tools.get_adjacency_matrix(self.edges, self.num_nodes)
        self.A_binary_with_I = tools.get_adjacency_matrix(self.edges + self.self_loops, self.num_nodes)
        self.A_norm = tools.normalize_adjacency_matrix(self.A_binary_with_I)
        # self.A1 = tools.get_spatial_graph(num_node, self_link, inward, outward)
