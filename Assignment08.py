# Analysis of Algorithms (CSCI 323)
# Winter 2025
# Assignment 8 - "Shortest Path Algorithms"
# Brandon Marsh

# Acknowledgements:
# I worked with the class


from random import randint, random
import Assignment02 as as2
import Assignment07 as as7
import Assignment09 as as9
import numpy as np
INF = 9999
from time import time


def random_weighted_graph(n,min_w,max_w,p_edge,directed=True):
    matrix = [[randint(min_w, max_w) if i != j and random() < p_edge else INF for j in range(n)] for i in range(n)]
    if not directed:
        matrix = [[matrix[i][j] if i < j else matrix[j][i] for j in range(n)] for i in range(n)]
    return matrix


def min_dist(dist, visited, src,n):
        min = INF
        min_index = -1
        for v in range(n):
            if dist[src][v] < min and not visited[v]:
                min = dist[src][v]
                min_index = v
        return min_index


def run_algs(algs, sizes, trials):
    p_edge = 1
    dict_algs = {}
    for alg in algs:
        dict_algs[alg.__name__] = {}
    for size in sizes:
        for alg in algs:
            dict_algs[alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            matrix = random_weighted_graph(size,10,99,p_edge,False)
            for alg in algs:
                start_time = time()
                mst = alg(matrix, size)
                end_time = time()
                net_time = end_time - start_time
                dict_algs[alg.__name__][size] += 1000 * net_time
                if size == sizes[0]:
                    print(alg.__name__,mst_cost(mst),mst)


    return dict_algs


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def kruskal_mst(matrix,n):
    result = []
    i = 0
    e = 0
    edges = edge_set(matrix,False)
    edges = sorted(edges, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(n):
        parent.append(node)
        rank.append(0)
    while e < n - 1:
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    return result

def edge_set(matrix, directed):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < INF:
                if directed or i < j:
                    edges.append((i, j,matrix[i][j]))
    return edges

def min_key(key, mstSet,n):
    min_k = INF
    min_idx = -1
    for v in range(n):
        if key[v] < min_k and not mstSet[v]:
            min_k = key[v]
            min_idx = v
    return min_idx

def prim_mst(matrix,n):
    key = [INF] * n
    parent = [None] * n
    key[0] = 0
    mstSet = [False] * n
    parent[0] = -1
    for _ in range(n):
        u = min_key(key, mstSet,n)
        mstSet[u] = True
        for v in range(n):
            if not mstSet[v] and key[v] > matrix[u][v]:
                key[v] = matrix[u][v]
                parent[v] = u
    mst = [(parent[i], i, matrix[i][parent[i]]) for i in range(1,n)]
    return mst


def mst_cost(mst):
    return sum([mst[i][2] for i in range(len(mst))])


def main():
    assn = "Assignment08"
    algs = [kruskal_mst,prim_mst]
    trials = 10
    sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    dict_algs = run_algs(algs, sizes, trials)
    as2.print_times(dict_algs, f"{assn}.txt")
    as2.plot_times(dict_algs, sizes, trials, algs, f"{assn}.png")



if __name__ == "__main__":
    main()