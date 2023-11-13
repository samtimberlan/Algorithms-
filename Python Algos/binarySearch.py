from typing import List


class BinarySearch:
    def find(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == target: return arr[mid]
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_boundary(arr: List[bool]) -> int:
        left, right = 0, len(arr) -1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid]: 
                right = mid - 1 # Move left
                ans = mid
            else: left = mid + 1 # Move right
                
        return ans

    def first_not_smaller(arr: List[int], target: int) -> int:
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target: 
                ans = mid
                right = mid - 1
            else:
                left = mid + 1        
        return ans

    def first_not_smaller(arr: List[int], target: int) -> int:
        left, right, ans = 0, len(arr) - 1, -1
        for num in range(left, right):
            mid = (left + right) // 2
            if arr[mid] >= target: 
                ans = mid
                right = mid - 1
            else:
                left = mid + 1        
        return ans

    def find_first_occurrence(arr: List[int], target: int) -> int:
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target: 
                ans = mid
                right = mid - 1
            else:
                left = mid + 1        
        return ans

    def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
        left, right, ans = 0, len(arr) -1, -1
        while left <= right:
            mid = (left+right) // 2
            if mid != 0 and mid != len(arr)-1  and arr[mid] > arr[mid-1] and arr[mid] > arr[mid + 1]:
                ans = mid
                return ans
            elif mid != 0 and mid != len(arr)-1 and arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def min_ship_capacity(nrt: List[int], wrk: int):
        l = max(nrt)
        r = sum(nrt)
        ans = -l

        while l <= r:
            mid = (l+r) // 2
            if BinarySearch.can_read(nrt, mid, wrk):
                r = mid - 1 #move left
                ans = mid
            else:
                l = mid + 1 #move right
        return ans

    def can_read(nrt, mid, wrk):
        acc = 0
        time_taken = 1

        for r in nrt:
            acc += r
            if acc > mid:
                time_taken += 1
                acc = r
            
        return time_taken <= wrk



print('find', BinarySearch.find([1,234,565], 565))
print('find boundary', BinarySearch.find_boundary([True, True, True, True, True]))
print('first occurrence', BinarySearch.find_first_occurrence([2, 3, 5, 7, 11], 7))
print('mountain array', BinarySearch.peak_of_mountain_array([0,10,3,2,1,0]))
print('min ship capacity', BinarySearch.min_ship_capacity([7,2,5,10,8], 2))