from collections import defaultdict
from typing import DefaultDict, List

def insertion_sort(unsorted_list: List[int]) -> List[int]:
    for i, value in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            temp = unsorted_list[current]
            unsorted_list[current] = unsorted_list[current - 1]
            unsorted_list[current - 1] = temp
            current -= 1
    return unsorted_list

def insertion_sort_2(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list

def selection_sort(list : List[int]) -> List[int]:
    for i, val in enumerate(list):
        min_idx = i
        for sort_item_idx in range(i, len(list)):
            if list[sort_item_idx] < list[min_idx]:
                list[sort_item_idx], list[min_idx] = list[min_idx], list[sort_item_idx]
    return list

def selection_sort_2(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        min_indx = i
        for j in range(i,len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_indx]:
                min_indx = j
        unsorted_list[i], unsorted_list[min_indx] = unsorted_list[min_indx], unsorted_list[i]
    return unsorted_list

# def bubble_sort(unsorted_list: List[int]) -> List[int]:
#     for i, entry in enumerate(unsorted_list):
#         for item in unsorted_list:
#             if entry < item:

def merge_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    midpoint = n // 2
    left_list, right_list = merge_sort(unsorted_list[:midpoint]), merge_sort(unsorted_list[midpoint:])
    result_list = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
    return result_list

# Using built-in sort methods
print(" ")
print("----------")

l = [5,343,2,134,76,8]
m = [32,21,5,65]
o = ["zebra", "fat", "apply", "lion", "ink"]

l.sort() # sorts the list in place
n = sorted(m) # sorts the list and returns result in new list
p = sorted(o, reverse=True)

print(l,m,p)

# Custom sort
print("----------")
print(" ")

dict = {"sch": 1, 'dea': 122, 'fre': 5, 'weui': 13, 'brts': 3}
priorities = [
    ("sch",1), 
    ('zea', 122), 
    ('fre', 5), 
    ('weui', 13), 
    ('brts', 3),
    ("sch",122),
    ('bbts', 6),
    ('brts', 2)
] # list of tuples

# the index number passed to 'priority' argument tallies with the undex number of the tuple elements
priorities.sort(key=lambda priority: (priority[0]))
print('Sort by key alone', priorities)

priorities.sort(key=lambda priority: (priority[1]))
print('Sort by value alone', priorities)

priorities.sort(key=lambda priority: (priority[0], priority[1]) )
print('Sort both by key and value. Key first', priorities)

priorities.sort(key=lambda priority: (priority[1], priority[0]) )
print('Sort both by key and value. Value first', priorities)

print("----------")
print(" ")

ordered_str = 'dba'
str= 'abcdefg'

# This sorting is performed by using a dictionary lookup to use numbers and pass those numbers to the sorted function. Once all the values from ordered_str have been gotten, sorting continues normally from ordered_str len.
def exclSort(str, order):
    ddict = defaultdict()
    for i,char in enumerate(order):
        ddict[char] = i
    return sorted(str, key=lambda x: ddict.get(x,len(ordered_str)))

print('Excl sort', exclSort(str, ordered_str))
    




print("----------")
print(" ")

order_list = ['#56', '#2', '#15232', '#19']
#order_list = ['#56', '#2', '#15232', '#19']
print('Basic sorting:', sorted(order_list))

len_sort = sorted(order_list, key=len)
print('Sorted by Length function:', len_sort)

def custom_sort_func(str):
    return int(str[1:])

custom_sort = sorted(order_list, key=custom_sort_func)
print('Custom sort:', custom_sort)



# unsorted_list = [int(x) for x in input().split()]
# res = insertion_sort_2(unsorted_list)
# print(' '.join(map(str, res)))

print("----------")
print(" ")

if __name__ == '__main__':
    unsorted_list = [6,3,1,76,2]
    res = selection_sort(unsorted_list)
    #print(' '.join(map(str, res)))
    #print(res)
    #selection_sort_2([2,43,8947,1])
    selection_sort(unsorted_list)

