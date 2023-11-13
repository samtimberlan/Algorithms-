from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        result = []
        lookup = {}

        for key, value in enumerate(nums):
            diff = target - value
            print(lookup.get(diff))
            if diff in lookup.values(): 
                result.append(diff)
                result.append(value)
                return result
            lookup[key] = value
        
        return result

    def maxProfit(prices: List[int]) -> int:
        l, r, maxProfit = 0, 1, 0

        while r < len(prices):
            if prices[r] > prices[l]: 
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r
            r += 1
        return maxProfit



    def containsDuplicate(nums: List[int]) -> bool:
        if len (set(nums)) == len(nums): print('false')
        else: print(True)


    def productExceptSelf(nums: List[int]) -> List[int]:
        multiplier = 1
        res = nums.copy()

        for key, num in enumerate(nums):
            nums[key] = multiplier
            multiplier *= num

        i = len(nums) - 1
        multiplier = 1

        while i >= 0:
            nums[i] *= multiplier
            multiplier *= res[i] 
            i -= 1

        return nums


    def remove_duplicates(arr: List[int]) -> int:
        l,r = 0,1
        
        while r < len(arr):
            if arr[l] != arr[r]: 
                l += 1
                arr[l] = arr[r]
            r += 1
        print(arr[:l+1])

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next
    
    N5 = Node(5)
    N4 = Node(4,N5)
    N3 = Node(3,N4)
    N2 = Node(2,N3)
    N1 = Node(1,N2)
    def middle_of_linked_list(head:Node) -> int:
        mid = 0
        while head and head.next:
            mid += 1
            head = head.next.next
        return mid


Solution.twoSum(nums = [2,7,11,15], target = 9)
Solution.maxProfit(prices =[7,1,5,3,6,4])
Solution.productExceptSelf(nums = [1,2,3,4])
Solution.remove_duplicates(arr = [1,2,3,4])
Solution.remove_duplicates(arr = [1,2,2,3,4,4])
Solution.middle_of_linked_list(Solution.N1)