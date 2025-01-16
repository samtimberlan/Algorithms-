Answering Questions:
Clarify
1. Give approach
2. Talk time complexity
3. Give another approach
4. Talk time complexity
5. Ask which approach should be coded
6. Talk about input validation and testcases
7. Add a testcase
8. Talk about tradeoffs and rationale for using data structures
9. Explain code when writing
10. Dry run

# Questions
Team
Balancing speed with accuracy

# Clarifying questions. Return type. Params.
For integers:
1. "What happens when an integer exceeds the max size on your platform?"
2. "How does your code handle division when the denominator could be zero?"
3. "Do you need floor division or regular division for this calculation?"

For strings:
1. "What character encoding is expected for the input/output?"
2. "Is string concatenation performance critical in this case?"
3. "Should empty strings be treated the same as null values?"

For lists:
1. "Will the list length change during iteration?"
2. "Do nested objects need to be copied independently?"
3. "Are you certain all list indices will be within valid bounds?"

# Merge Intervals. Sort. Compare start and end times
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        

# DFS pseudocode for top-sort

# Prefix sum
def prefix_sums(arr):
    # Pre-allocate exact size needed
    prefix = [0] * (len(arr) + 1)
    
    # Use enumerate to avoid separate index arithmetic
    for i, num in enumerate(arr, 1):
        prefix[i] = prefix[i - 1] + num
        
    return prefix


# BACKTRACKING
def backtrack(node, state):
            if state is a solution:
                res.append(state.copy()) # deep copy
                return

            for el in range:
                if el is one of the solutions:
                    state.apend(el)
                    backtrack(node + 1, state)
                    state.pop(el)

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # need to sort
        
        def backtrack(idx, path):
            res.append(path.copy())

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]: # check that the value at the current index is not the same as the previous s
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        res = []
        backtrack(0, [])
        return res


class Solution:
    def calculate(self, expression: str) -> int:
        # Initialize variables to track current state
        # curr_num: builds current number digit by digit
        # prev_num: stores last processed number after operation
        # running_sum: accumulates addition/subtraction results
        # curr_operator: stores operator to apply to next number
        curr_num, prev_num, running_sum, curr_operator = 0, 0, 0, '+'
        
        # Add '+' to handle the last number in expression
        # This trick ensures last number gets processed
        for char in expression + '+':
            # Skip any whitespace characters
            if char == ' ':
                continue
            
            # If character is a digit, build number
            # Example: "23" -> first 2 (curr_num=2), then 3 (curr_num=23)
            if char.isdigit():
                curr_num = 10 * curr_num + int(char)
                continue
            
            # When we hit an operator, process previous operation
            # '+': Add prev_num to running_sum, store curr_num
            if curr_operator == '+':
                running_sum += prev_num  # Add previous number to result
                prev_num = curr_num      # Store current number for next operation
                
            # '-': Add prev_num to running_sum, store -curr_num
            elif curr_operator == '-':
                running_sum += prev_num  # Add previous number to result
                prev_num = -curr_num     # Store negative of current number
                
            # '*': Multiply prev_num and curr_num, store result
            elif curr_operator == '*':
                prev_num = prev_num * curr_num  # Multiply numbers directly
                
            # '/': Divide prev_num by curr_num, store result
            elif curr_operator == '/':
                # Use int division, truncate toward zero
                prev_num = int(prev_num / curr_num)
            
            # Reset current number and store new operator
            curr_num = 0          # Reset for next number
            curr_operator = char  # Store operator for next operation
        
        # Add final prev_num to running_sum for result
        # This handles the last number processed
        return running_sum + prev_num


# Binary Exponentiation for Pow
The basic idea here is to use the fact that x**n can be expressed as:
(x ** 2) ** (n/2) if n is even
x*(x ** 2) ** (n−1)/2 if n is odd (we separate out one x, then n−1 will become even)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: anything raised to 0 is 1
        if n == 0:
            return 1

        # Handle negative exponents
        # Example: x^(-2) = (1/x)^2
        # Convert to positive exponent by:
        # 1. Taking reciprocal of base (x)
        # 2. Making exponent positive
        if n < 0:
            n = -1 * n
            x = 1 / x

        # Initialize result to 1 (multiplicative identity)
        # This will store our running product
        result = 1

        # Continue until exponent becomes 0
        while n != 0:
            # If exponent is odd:
            # 1. Multiply result by current x
            # 2. Decrease n by 1 to make it even
            # Example: x^5 = x * x^4
            if n % 2 == 1:
                result *= x
                n -= 1

            # Square the base (x = x * x)
            # Halve the exponent (n = n / 2)
            # Example: x^4 = (x^2)^2
            x *= x
            n //= 2

        return result


# ProductOfArrayExceptSelf
This is the "Product of Array Except Self" problem where you need to return an array such that each element is the product of all numbers in the array except itself.
Let's use the example array [1, 2, 3, 4] to understand how it works:

First Loop (Left to Right): # [1, 1, 2, 6]
After this loop, each position contains the product of all numbers to its left.

Second Loop (Right to Left): # [24, 12, 8, 6]
The variable R keeps track of the running product from the right side. For each position, we:

Multiply the current answer (product of left numbers) by R (product of right numbers)
Update R by multiplying it with the current number

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 2, 3, 4]
        [24, 12, 8, 6]
        # The length of the input array
        length = len(nums)
        answer = [0] * length # [0, 0, 0, 0]
        answer[0] = 1 # [1, 0, 0, 0]
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1] # [1, 1, 2, 6]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i] # [24, 12, 8, 6]

        return answer

# LCA. Exploits BST property of left < node < right 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root

        while node:
            if p.val > node.val < q.val:
                node = node.right
            elif p.val < node.val > q.val:
                node = node.left
            else:
                return node

# Matrix BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for r_idx, r_val in enumerate(grid):
            sub = r_val
            for c_idx, c_val in enumerate(sub):
                if c_val == '1':
                    islands += 1
                    self.bfs(grid, r_idx, c_idx)
        return islands

    def bfs(self, grid, r, c):
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

                if 0 <= nr < row_count and 0 <= nc < col_count and grid[nr][nc] == '1':
                    #can either reset land to water or use a visited set
                    grid[nr][nc] = '0'
                    q.append([nr, nc])


# Kth Positive
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_digit_index = -1
        swap_idx_1 = -1
        swap_idx_2 = -1

        # Traverse the string from right to left, tracking the max digit and
        # potential swap
        for i in range(n - 1, -1, -1):
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                max_digit_index = i  # Update the index of the max digit
            elif num_str[i] < num_str[max_digit_index]:
                swap_idx_1 = i  # Mark the smaller digit for swapping
                swap_idx_2 = (
                    max_digit_index  # Mark the larger digit for swapping
                )

        # Perform the swap if a valid swap is found
        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = (
                num_str[swap_idx_2],
                num_str[swap_idx_1],
            )

        return int(
            "".join(num_str)
        )  # Return the new number or the original if no
        # swap occurred

# Vertical order traversal of a binary tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col = 0
        q = deque([(root, col)])
        lookup = defaultdict(list)

        while q:
            node, col = q.popleft()

            if node:
                lookup[col].append(node.val)
                q.append((node.left, col-1))
                q.append((node.right, col+1))

        return [lookup[x] for x in sorted(lookup.keys())]

# improved to remove sorting using min and max ranges:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        col = 0
        q = deque([(root, col)])
        lookup = defaultdict(list)
        min_column = max_column = 0

        while q:
            node, col = q.popleft()

            if node:
                lookup[col].append(node.val)
                min_column = min(min_column, col)
                max_column = max(max_column, col)

                q.append((node.left, col-1))
                q.append((node.right, col+1))

        return [lookup[x] for x in range(min_column, max_column + 1)]


# Lowest common ancestor (LCA) of a binary tree with parent pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1

# Lowest common ancestor (LCA) of a binary tree without parent pointer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        if not curr or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(curr.left, p, q)
        right = self.lowestCommonAncestor(curr.right, p, q)

        if left and right:
            return curr

        return left or right

# Sum root to leaf
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        root_to_leaf: int = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf

# NestedList

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += bfs(nested.getList(), depth + 1)
            return total   

        def bfs(nested_list):
            q = deque(nested_list)   
            depth, tot = 1, 0

            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    print(node)
                    if node.isInteger():
                        tot += node.getInteger() * depth
                    else:
                        q.append(node.getList())
                    

        #return dfs(nestedList, 1)
        return bfs(nestedList)
        
        

