# Node implementation
from collections import deque
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

    def dfs_iterative(root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.value)
            # Push right first so that left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
    
    def bfs(root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result