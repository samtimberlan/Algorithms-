graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}

def rec_dfs(graph, curr_node):
    if curr_node is None: return 

    print(curr_node)

    for node in graph[curr_node]:
        rec_dfs(graph, node)

def itr_dfs(graph, curr_node):
    stack = [curr_node]
    
    while len(stack) > 0:
        curr = stack.pop()
        print(curr)

        for child_node in graph[curr]:
            stack.append(child_node)

def bfs(graph, curr_node):
    queue = [curr_node]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node)

        for child_node in graph[node]:
            queue.append(child_node)

def has_path(graph:dict, curr_node:str, target:str):
    queue = [curr_node]

    while len(queue) > 0:
        node = queue.pop(0)
        if node == target.lower(): return True

        for child_node in graph[node]:
            queue.append(child_node)

    return False




#rec_dfs(graph, 'a')
#itr_dfs(graph, 'a')
#bfs(graph, 'a')
print(has_path(graph, 'a', 'A'))