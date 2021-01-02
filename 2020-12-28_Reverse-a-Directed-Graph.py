"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a directed graph, reverse the directed graph so all directed edges are reversed.

Example:
Input:
A -> B, B -> C, A ->C

Output:
B->A, C -> B, C -> A
"""

from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

def reverse_graph(graph):
    # Fill this in.
    # rev_graph = {}
    visited = set()
    for u in graph.values():
        for v in u.adjacent:
            if v not in visited:
                u.adjacent.remove(v)
                v.adjacent.append(u)
        visited.add(u)
    return graph

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

reverse_graph(graph)

for key, val in reverse_graph(graph).items():
    print(key,[x.value for x in val.adjacent])
