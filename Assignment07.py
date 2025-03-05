# Analysis of Algorithms (CSCI 323)
# Winter 2025
# Assignment 7 - "Graphs and Graph Algorithms"
# Brandon Marsh

# Acknowledgements:
# I worked with the class


import numpy as np
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from random import random



#[1] Define a function read_graph(file_name) that reads a graph from a text file and returns an adjacency/cost matrix.
def read_graph(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
        print(lines)
        graph = [[int(x) for x in line.strip().split(" ")] for line in lines]
        return graph


#[2] Define a function adjacency_table(matrix) that accepts a graph as an adjacency/cost matrix and returns an adjacency/cost table.
def adjacency_table(matrix):
    n = len(matrix)
    table = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                table[i].append(j)
    return table


def print_adjacency_matrix(matrix):
    print(np.array(matrix))


def print_adjacency_table(table):
    n = len(table)
    for i in range(n):
        print(i, "\t", table[i])


#[3] Define a function edge_set(matrix) that accepts a graph as an adjacency/cost matrix and returns an edge/cost set.
def edge_set(matrix, directed):
    n = len(matrix)
    edges = set()
    table = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                if directed or i < j:
                    edges.add((i, j))
    return edges


#[4] Define a function edge_map(matrix) that accepts a graph as an adjacency/cost matrix and returns an edge/cost set.
def edge_map(matrix):
    n = len(matrix)
    map = {}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                map[(i, j)] = 1
    return map


def is_undirected(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                return False
    return True


def random_graph(n, directed, p):
    matrix = [[1 if random() < p else 0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    if not directed:
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j] = matrix[j][i]
    return matrix


def bfs(matrix, s, visited):
    q = []
    n = len(matrix)
    visited.append(s)
    q.append(s)
    while q:
        curr = q.pop(0)
        for j in range(n):
            if matrix[curr][j] != 0 and j not in visited:
                visited.append(j)
                q.append(j)


def bfs_main(matrix):
    visited = []
    for i in range(len(matrix)):
        if i not in visited:
            bfs(matrix, i, visited)
    return visited


def dfs(matrix, s, visited):
    n = len(matrix)
    visited.append(s)
    for j in range(n):
        if matrix[s][j] != 0 and j not in visited:
            dfs(matrix, j, visited)


def dfs_main(matrix):
    visited = []
    for i in range(len(matrix)):
        if i not in visited:
            dfs(matrix, i, visited)
    return visited



def draw_graph(edges, directed, filename):
    g = nx.DiGraph()
    g.add_edges_from(edges)
    val_map = {'A': 1.0, 'D': 0.5714285714285714, 'H': 0.0}
    values = [val_map.get(node, 0.25) for node in g.nodes()]
    pos = nx.spring_layout(g)
    cmap = plt.get_cmap('jet')
    nx.draw_networkx_nodes(g, pos, cmap=cmap, node_color=values, node_size=500)
    nx.draw_networkx_labels(g, pos, font_size=12, font_color='white')
    if directed:
        nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='r', arrows=directed, arrowsize=10)
    else:
        nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='r', arrows=False)

    plt.savefig(filename)
    plt.show()


def do_graph(assn, desc, matrix):
    table = adjacency_table(matrix)
    directed = True
    edges = edge_set(matrix, directed)
    map_edges = edge_map(matrix)
    print("Adjacency Matrix: ")
    print_adjacency_matrix(matrix)
    print("Adjacency Table: ")
    print_adjacency_table(table)
    print("Edge Set: ")
    print(edges)
    print("Edge Map: ")
    print(map_edges)
    print("BFS Traversal: ",bfs_main(matrix))
    print("DFS Traversal: ",dfs_main(matrix))
    draw_graph(edges, directed, f"{assn}_{desc.replace(' ', '')}.png")


def main():
    assn = "Assignment07"
    matrix1 = read_graph(f"{assn}_Graph.txt")
    desc1 = "Graph from file"
    do_graph(assn, desc1, matrix1)
    matrix2 = random_graph(5, False, 0.8)
    desc2 = "Random Graph"
    do_graph(assn, desc2, matrix2)



if __name__ == "__main__":
    main()