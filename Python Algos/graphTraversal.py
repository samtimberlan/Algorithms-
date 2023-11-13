graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}

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

# With Lists
# edges = [
#     ['i', 'j'],
#     ['k', 'i'],
#     ['m', 'k'],
#     ['k', 'l'],
#     ['o', 'n']
# ]

def build_graph(edges):
    graph = {}

    for edge in edges:

        # With destructturing

        (a,b) = edge
        
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)


        #Without destructuring

        # if edge[0] not in graph: graph[edge[0]] = []
        # if edge[1] not in graph: graph[edge[1]] = []

        # graph[edge[0]].append(edge[1])
        # graph[edge[1]].append(edge[0])

    return graph

def recursive_dfs(graph, current_node, result):
    if current_node is None:
        return

    # Do work
    result.append(current_node) 
    
    for neighbor in graph[current_node]:
        recursive_dfs(graph, neighbor, result)

    return result

def iterative_dfs(graph, current_node):

    # Initialize stack with first item
    stack = [current_node]

    result = []

    # cannot use this. Python does not allow the use of "for loop" in a dynamically changing DS.
    #  for item in range(len(stack)):

    # Can only use while loop
    while len(stack) > 0:

        # Remove and save last node from stack
        current = stack.pop()

        # Do work
        result.append(current) 

        for neighbor in graph[current]:

            # Add the item's children to the stack
            stack.append(neighbor)

    return result

def bfs(graph, current_node):
    queue = [current_node]   
    result = []     

    while len(queue):
        current = queue.pop(0)

        # Do work
        result.append(current) 

        for neighbor in graph[current]:
            queue.append(neighbor)

    return result

def has_path(graph, current_node, destination):
    
    if current_node == destination:
        return True
    
    for node in graph[current_node]:
        if has_path(graph, node, destination): return True

    return False    

def has_path_bfs(graph, current_node, destination):
    queue = [current_node]
    graph = build_graph(edges)

    while len(queue) > 0:
        current = queue.pop(0)
        if current == destination: return True

        for node in graph[current]:
            queue.append(node)
    return False

def has_path_bfs(graph:dict, current_node:str, destination:str, visited_nodes:set):
    queue = [current_node]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == destination.lower(): return True

        # Mark the current node as visited
        visited_nodes.add(current)

        for child_node in graph[current]:

            # Add only child nodes that have not been visited. Resolves infinite loop
            if child_node not in visited_nodes: 
                queue.append(child_node)

    return False

def has_path_undirected(current_node, destination):
    graph = build_graph(edges)
    visited_nodes = set()

    return has_path_bfs(graph, current_node, destination, visited_nodes)

def count_paths():
    graph = build_graph(edges)
    separate_graph_count = 0
    visited_nodes = set()

    for node in graph:
        if dfs_with_undirected_graph(graph, node, visited_nodes):
            separate_graph_count += 1

    return separate_graph_count

def dfs_with_undirected_graph(graph:dict, root_node:str, visited_nodes:set):
    if root_node in visited_nodes: return False

    visited_nodes.add(root_node)

    for node in graph[root_node]:
        dfs_with_undirected_graph(graph, node, visited_nodes)

    return True

def find_largest_connected_component(graph: dict, root_node: str):
    largest = 0
    visited_nodes = set()

    for parent_node in graph:
        result = []
        connected_count = count_dfs_traversal(graph, parent_node, visited_nodes, result)
        if connected_count > largest: largest = connected_count

    return largest

def count_dfs_traversal(graph: dict, root_node:str, visited_nodes:set, result:list):
    if root_node in visited_nodes: return 0

    result.append(root_node) 
    visited_nodes.add(root_node)

    for node in graph[root_node]:
        count_dfs_traversal(graph, node, visited_nodes, result)

    return len(result)

def shortest_path_and_distance(graph:dict, root_node, target):
    queue, distance, visited, path = [root_node], 0, set(), []

    while len(queue) > 0:
        node = queue.pop(0)

        if node is target: return (path, distance)

        visited.add(node)
        distance += 1
        path.append(node)

        for child_node in graph[node]:
            if child_node not in visited: queue.append(child_node)
    
    return ([], -1)

def count_connected_islands_matrix(graph:list):
    count, visited = 0, set()

    for r, row in enumerate(graph):
        for c, column in enumerate(row):
            if dfs_count_connected_islands_matrix(graph, column, r, c, visited): count += 1

def dfs_count_connected_islands_matrix(graph:list, current_node:str, row_index:int, col_index:int, visited:set):
    is_valid_row_index = 0 <= row_index < len(graph)
    is_valid_col_index = 0 <= col_index < len(graph)

    if not is_valid_row_index or not is_valid_col_index: return False

    position = str(row_index) + ',' + str(col_index)
    stack = [position]

    while len(stack) > 0:
        node_position = stack.pop()

        if node_position in visited: return False
        if current_node == 'W': return False
        
        visited.add(position)

        for child_node in graph[row_index - 1][col_index]:
            if position not in visited: stack.append(child_node)
        
        for child_node in graph[row_index + 1][col_index]:
            if position not in visited: stack.append(child_node)

        for child_node in graph[row_index][col_index - 1]:
            if position not in visited: stack.append(child_node)

        for child_node in graph[row_index][col_index + 1]:
            if position not in visited: stack.append(child_node)

    return True



    


print('Recursive DFS', recursive_dfs(graph, 'a', []))
print('Iterative DFS', iterative_dfs(graph, 'a'))
print('BFS', bfs(graph, 'a'))
print('Has Path', has_path(graph, 'a', 'f'))
#print('Has Path BFS', has_path_bfs(graph, 'a', 'f'))
print('Build graph', build_graph(edges))
print('Has Path Undirected', has_path_undirected('a', 'f'))
print('Separated graph count:', count_paths())
print('largest connected count:', find_largest_connected_component(graph=build_graph(edges), root_node='a'))
print('Shortest path and distance:', shortest_path_and_distance(graph=build_graph(edges), root_node='a', target='j'))
print('Count connected islands:', count_connected_islands_matrix(graph=[['L', 'L', 'L'], ['L', 'L', 'L'], ['L', 'L', 'L']]))