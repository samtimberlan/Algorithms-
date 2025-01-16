from collections import deque 

def build_order(projects, dependencies):
    graph = {project: [] for project in projects}
    result = []
    for project, dependency in dependencies:
        graph[project].append(dependency)

    return build(graph, project, result)

def build(graph, node, result):
    visited = set()
    if not node:
        return
    result.append(node)
    visited.add(node)

    for dependent in graph[node]:
        if node not in visited:
            build(graph, node, result)

    return result



def numIslands(grid) -> int:
    islands = 0

    for r_idx, r_val in enumerate(grid):
        sub = r_val
        for c_idx, c_val in enumerate(sub):
            if c_val == '1':
                islands += 1
                bfs(grid, r_idx, c_idx)
    return islands

def bfs(grid, r, c):
    row_count, col_count = len(grid), len(grid[0])
    q = deque([[r, c]])
    
    # top, left, right, bottom
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    

    while q:
        node = q.popleft()

        # check all directions
        for dir in dirs:
            nr = node[0] + dir[0]
            nc = node[1] + dir[1]

            # check bounds and 1
            cell = grid[nr][nc]

            if 0 <= nr < row_count and 0 <= nc < col_count and cell == '1':
                #can either reset land to water or use a visited set
                grid[nr][nc] = '0'
                q.append([nr, nc])



grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid=grid))




projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
print(build_order(projects=projects, dependencies=dependencies))
