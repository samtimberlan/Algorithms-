import itertools

def merge_sort(lst):
    end = len(lst) - 1
    mid=end // 2
    if end <= 1:
        return lst
    left, right = merge_sort(lst[:mid]), merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    l,r,temp = 0,0,[]
    while l < len(left) or r < len(right):
        if l > len(left) - 1:
            temp.append(right[r])
            r+=1
        elif r > len(right) - 1:
            temp.append(left[l])
            l+=1
        elif left[l] <= right[r]:
            temp.append(left[l])
            l+=1
        elif left[l] > right[r]:
            temp.append(right[r])
            r+=1
    return temp


def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def flip(r,c,matrix):
            #flip rows
            matrix[r] = [0 for _ in matrix[r]]
            for row in matrix:
                row[c] = 0
            #matrix = [x[c] = 0 for x in matrix]
        def setZeroes_prv(r,c,matrix): 
            if r >= len(matrix): return
            if c >= len(matrix[r]): setZeroes_prv(r+1, 0, matrix)
            if matrix[r][c] == 0:
                flip(r,c,matrix)
            setZeroes_prv(r, c+1, matrix)

        setZeroes_prv(0,0,matrix)

# print(" ")
# print("----------")
# l = [5,343,2,134,76,8]
# #print("merge sort", merge_sort(l))
# print("merge sort", merge_sort([5,1]))

# print("----------")
# print(" ")

# print('set zeroes:', setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

print(len('abc'))


def generate_permutaions(elem):
    return list(itertools.permutations(elem))
    #return itertools.permutations(elem)

def generate_combinations(elem):
    return list(itertools.combinations(elem, 2))

print('perm', generate_permutaions([3,4,5,2]))
print('combi', generate_combinations([3,4,5,2]))


[['a', 'b'], ['b', 'c']]
def build_undirected_adjacency_list(arr): # typically have cycles
    graph = defaultdict(list)

    for el in arr:
        node, child = el
        graph[node].append(child)
        graph[child].append(node)

[['a', 'b'], ['b', 'c']]
def build_directed_adjacency_list(arr):
    graph = defaultdict(list)

    for el in arr:
        node, child = el
        graph[node].append(child)

    return graph

def itr_directed_dfs(graph, node):
    stack = deque([node])

    while stack:
        curr = stack.pop()
        print(curr)

        for neighbor in graph.get(curr):
            stack.append(neighbor)

def directed_dfs(graph, node):
    if not node:
        return
    
    print (node)

    for neighbor in graph.get(node):
        dfs(graph, neighbor)

def bfs(graph, node):
    q = deque([node])

    while q:
        curr = q.popleft()

        print(curr)

        for neighbor in graph[curr]:
            q.append(neighbor)

def directed_has_path(graph, node, target):
    def bfs(graph, node, target):
        q = deque([node])

        while q:
            curr = q.popleft()
            if curr == target: return True
            for el in graph[curr]:
                q.append(el)

    return False

# undirected needs a visited set to avoid cycles 
def itr_dfs_undirected_has_path(graph, node, target, visited):
    if node in visited: return
    if node == target: return True
    visited.add(node)

    stack = deque([node])

    while stack:
        curr = stack.pop()
        for el in graph.get(curr):
            stack.append(el)
    return False

def undirected_bfs_connected_components(graph):
    visited, count = set(), 0
    for el in graph.keys():
        if undirected_bfs(graph, el, visited):
            count += 1
    return count

def undirected_bfs(graph, node, visited):
        q = deque([node])

        while q:
            curr = q.popleft()
            if curr in visited: return False
            visited.add(curr)
            for el in graph.get(curr):
                q.append(el)
        return True

def undirected_largest_component(graph):
    largest, visited = 0, set()
    for node in graph.keys():
        largest = max(undirected_rec_dfs(graph, node, visited), largest)
    return largest

def undirected_rec_dfs(graph, node, visited):
    # if not node can be removed because the func is called from a loop with a given graph size. It will not cause cycles
    if not node or node not in visited: return 0
    visited.add(node)

    for neigbor in graph.get(node, []):
        return undirected_rec_dfs(graph, neigbor, visited) + 1
    
# shortest path problems must be bfs traversal
def undirected_shortest_path(graph, src, dest):
    def bfs(graph, src, dest, visited):
        node = src
        count = 0
        q = deque([node, count])

        while q:
            curr, dist = q.popleft()
            if node not in visited: 
                visited.add(node)
                if curr == dest: return [curr, dist]

            for el in graph[curr]:
                q.append([el, count+1])
        return [None, -1]
    shortest_dist = 0
    for el in graph.keys():
        shortest_dist = min(bfs(graph, src, dest), shortest_dist)











