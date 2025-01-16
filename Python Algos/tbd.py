from collections import defaultdict
from typing import DefaultDict, List

# Graph
# With tuples
edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n'),
    ('a', 'i'),
    ('b', 'c'),
    ('c', 'd'),
    ('y', 'z')
]

# build undirected adjacency matrix from array
def build_graph(edges: list) -> dict:
    graph = defaultdict(list)
    for el in edges:
        graph[el[0]].append(el[1])
        graph[el[1]].append(el[0])

    return graph

def recursive_dfs(graph, current_node, result, seen):
    # base case
    if current_node in seen:
        return result

    # unit of work
    seen.add(current_node)
    result.append(current_node)

    # recurse on neighbors
    for node in graph.get(current_node):
        recursive_dfs(graph, node, result, seen)

    return result


graph = build_graph(edges)
print('Recursive DFS', recursive_dfs(graph, 'a', [], set()))

