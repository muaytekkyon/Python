# Analysis of Algorithms (CSCI 323)
# Winter 2025
# Assignment 9 - "Shortest Path Algorithms"
# Brandon Marsh

# Acknowledgements:
# I worked with the class
from random import randint, random
import Assignment02 as as2
import numpy as np
INF = 9999
from time import time
import matplotlib.pyplot as plt

def random_weighted_graph(size,min_w,max_w,p_edge):
    return[[randint(min_w, max_w) if i != j and random() < p_edge else INF for j in range(size)] for i in range(size)]


# [1] Define a function floyd_apsp(graph) that solves APSP for a graph using Floyd's dynamic programming algorithm.
# See https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
def floyd_apsp(matrix,dist,pred,n):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]



# [2] Define a function bellman_ford_sssp(es, n, src) that takes an edge-set of the graph, the size of the graph, and a starting point, and solves SSSP using the Bellman Ford dynamic programming algorithm.
# See https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
def bellman_ford_sssp(matrix,edges,src,dist,pred,n):
    for i in range(n):
        for edge in edges:
            u, v, wt = edge
            if dist[src][u] + wt < dist[src][v]:
                dist[src][v] = dist[src][u] + wt
                pred[src][v] = u
    return dist


# [3] Define a wrapper function bellman_ford_apsp(graph) that converts the graph to an edge-set (using the function defined earlier), then calls bellman_ford_sssp for each of the n possible sources.
def bellman_ford_apsp(matrix,dist,pred,n):
    edges = edge_set(matrix)
    for i in range(n):
        bellman_ford_sssp(matrix,edges,i,dist,pred,n)


def init_dist_pred(matrix, n):
    pred = [[i for j in range(n)] for i in range(n)]
    dist = [[matrix[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        dist[i][i] = 0
        pred[i][i] = -1
    return dist, pred


# [4] Define a function dijkstra_sssp_matrix(graph, src) that takes a graph and a starting point, and solves SSSP using Dijsktra's greedy SSSP algorithm, assuming an adjacency matrix and minimization over an array.
# See https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7
def dijkstra_sssp(matrix, src, dist, pred, n):
     visited = [False] * n
     for i in range(n):
         x = min_dist(dist, visited, src,n)
         visited[x] = True
         for y in range(n):
             if not visited[y] and dist[src][y] > dist[src][x] + matrix[x][y]:
                    dist[src][y] = dist[src][x] + matrix[x][y]
                    pred[src][y] = x


def min_dist(dist, visited, src,n):
        min = INF
        min_index = -1
        for v in range(n):
            if dist[src][v] < min and not visited[v]:
                min = dist[src][v]
                min_index = v
        return min_index


def dijkstra_apsp(matrix,dist,pred,n):
    for i in range(n):
       dijkstra_sssp(matrix,i,dist,pred,n)


def edge_set(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < INF:
                edges.append((i, j, matrix[i][j]))
    return edges


# def draw_graph(edges, directed, filename):
#     g = nx.DiGraph()
#     g.add_edges_from(edges)
#     val_map = {'A': 1.0, 'D': 0.5714285714285714, 'H': 0.0}
#     values = [val_map.get(node, 0.25) for node in g.nodes()]
#     pos = nx.spring_layout(g)
#     cmap = plt.get_cmap('jet')
#     nx.draw_networkx_nodes(g, pos, cmap=cmap, node_color=values, node_size=500)
#     nx.draw_networkx_labels(g, pos, font_size=12, font_color='white')
#     if directed:
#         nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='r', arrows=directed, arrowsize=10)
#     else:
#         nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='r', arrows=False)
#
#     plt.savefig(filename)
#     plt.show()


def run_algs(algs, sizes, trials):
    dict_algs = {}
    for alg in algs:
        dict_algs[alg.__name__] = {}
    for size in sizes:
        for alg in algs:
            dict_algs[alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            matrix = random_weighted_graph(size,10,99,.3)
            for alg in algs:
                start_time = time()
                dist, pred = init_dist_pred(matrix, size)
                alg(matrix, dist, pred, size)
                end_time = time()
                net_time = end_time - start_time
                dict_algs[alg.__name__][size] += 1000 * net_time
                if size == sizes[0]:
                    print("\n", alg.__name__)
                    print_adjacency_matrix(dist)
                    print_adjacency_matrix(pred)

    return dict_algs


def print_adjacency_matrix(matrix):
    print(np.array(matrix))


def main():
    assn = "Assignment09"
    algs = [floyd_apsp, dijkstra_apsp, bellman_ford_apsp]
    trials = 1
    sizes = [10, 20, 30]
    dict_algs = run_algs(algs, sizes, trials)
    as2.print_times(dict_algs, f"{assn}.txt")
    as2.plot_times(dict_algs, sizes, trials, algs, f"{assn}.png")
    # matrix = random_weighted_graph(10,10,20,.3)
    # print_adjacency_matrix(matrix)
    # edges = edge_set(matrix)
    # print(edges)
    # dist, pred = init_dist_pred(matrix, size)
    # floyd_apsp(matrix, dist, pred,size)
    # print_adjacency_matrix(dist)
    # print_adjacency_matrix(pred)
    #
    # dist, pred = init_dist_pred(matrix, size)
    # bellman_ford_apsp(matrix, dist, pred,size)
    # print_adjacency_matrix(dist)
    # print_adjacency_matrix(pred)
    #
    # dist, pred = init_dist_pred(matrix, size)
    # dijkstra_apsp(matrix, dist, pred,size)
    # print_adjacency_matrix(dist)
    # print_adjacency_matrix(pred)



if __name__ == "__main__":
    main()