import heapq

def heap_sort(lst):
    result = []

    for el in lst:
        heapq.heappush(result, el)
    return [heapq.heappop(result) for i in range(len(result)) ]

def heap_sort_test(lst):
    heapq.heapify(lst)
    return [heapq.heappop(lst) for i in range(len(lst)) ]

def heap_nlargest(lst, n):
    #heapq.heapify(lst)
    a = heapq.nlargest(n, lst)

    return heapq.nlargest(n, lst)

lst = [3,6,10,1,2, 89]
print(heap_sort(lst))
print(heap_sort_test(lst))
print(heap_nlargest(lst, 2))
    