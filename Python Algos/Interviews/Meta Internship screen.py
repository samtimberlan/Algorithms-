"""
Implement a mock of cd (change directory) command on Unix. The code doesn't have to change actual directories, just return the new path after cd was executed.

The function takes two arguments (current working directory and directory to change to), and returns the output directory as if cd command was executed. There's no filesystem underneath; all paths are valid.


| cwd      | cd (arg)       | output
| -------- | -------------- | ------
| /        | foo            | /foo
| /baz     | /bar           | /bar
| /baz     | bar            | /baz/bar
| /foo/bar | ../../../../.. | /
| /x/y     | ../p/../q      | /x/q
| /x/y     | /p/./q         | /p/q
| /x/y     | /p/../q        | /q
"""

'''
'string
'valid input
'bazbar'\
' ./../

'''

'''
break string (/)
run
1. Chack arg for special chars
if / forget cwd and append it to cd. return
if . append cd to cwd with / in btw. retun
if .. get parent and append to cd. retun

get parent(arr.[tok], ind). 0.., 1.., ../../..
    retunr ind-1
get
'''


def change_directory(cwd: str, path: str) -> str:
    # If the path is absolute, start from root
    if path.startswith('/'):
        new_path = []
    else:
        # Otherwise, start from current working directory
        new_path = cwd.split('/')
    
    # Split the target path and process each part
    parts = path.split('/')
    
    for part in parts:
        if part == '' or part == '.':
            # Ignore empty or current directory
            continue
        elif part == '..':
            if new_path and new_path != ['']:
                new_path.pop()  # Move up one level if possible
        else:
            new_path.append(part)  # Add the new directory
    
    # Join the resulting parts into the final path
    result = '/' + '/'.join(filter(None, new_path))  # Filter removes empty parts
    
    return result if result != '' else '/'

# Edge Case Test Cases
print(change_directory('/', 'foo//bar'))          # Output: /foo/bar (ignore multiple slashes)
print(change_directory('/x/y', '../../../'))      # Output: / (too many .., stay at root)
print(change_directory('/x/y', 'p/../../../q'))   # Output: /q (too many .., then /q)
print(change_directory('/x/y', '/../..'))         # Output: / (can't move above root)
print(change_directory('/', '//////'))            # Output: / (multiple slashes collapse to root)

def simplifyPath(self, path: str) -> str:
        stack = []
    
        for part in path.split('/'):
            if part == '..' and stack:
                stack.pop()
            elif part not in set(['', '.', '..']):
                stack.append(part)
                
        return '/' + '/'.join(stack)




def locateEarliestMonth(stockPrice):
    # Write your code here
    min_val  = float('inf')
    result = 0
    seen = {}
    
    for i, price in enumerate(stockPrice):
        if price in seen:
            diff = abs(i - seen[price])
            if diff < min_val:
                min_val = diff
                result = i
        seen[price] = i
    return result + 1

print(locateEarliestMonth([5,1,3,2,4,5]))

# def min_abs_diff(arr):
#     min_diff = float('inf')
#     for i in range(len(arr) - 1):
#         diff = abs(arr[i] - arr[i + 1])
#         if diff < min_diff:
#             min_diff = diff
#     return min_diff

# # Test the function with the given array
# arr = [5, 1, 3, 2, 4, 5]
# result = min_abs_diff(arr)
# print(result)


# Follow-up interview
https://leetcode.com/problems/valid-word-abbreviation/solutions/5907529/validating-abbreviations-in-strings-a-two-pointer-approach/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days