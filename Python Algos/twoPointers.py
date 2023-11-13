from typing import List


def move_zeros(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

# def move_zeros(nums: List[int]) -> None:
#     l,r = 0,1
#     while r < len(nums):
#         if nums[l] != 0:
#             l += 1
#         if nums[r] != 0:
#             nums[l],nums[r] = nums[r],nums[l]
#         r += 1
#     return nums
#h

def two_sum_sorted(arr: List[int], target: int) -> List[int]:

    l,r = 0, len(arr) - 1
    while l < len(arr):
        sum = arr[l] + arr[r]
        if sum == target: return [l,r]
        if sum > target: 
            r -= 1
        elif sum < target:
            l += 1
    return []

def is_palindrome(s: str) -> bool:
    sa = list(s)
    sp = [x.lower() for x in sa if x.isalpha()]
    rsp = sp.copy()
    rsp.reverse()

    if sp == rsp:
        return True
    else:
        return False

def subarray_sum_fixed(nums: List[int], k: int) -> int:
    maxSum,l, winSum = 0, 0, 0
    r = k-1

    for i in range(k):
        winSum += nums[i]

    while r < len(nums):
        winSum -= nums[l]
        winSum += nums[r]
        maxSum = max(winSum, maxSum)
        r += 1
        l += 1

    return maxSum

def find_all_anagrams(original: str, check: str) -> List[int]:
    def isSame(winStr):
        return sorted(winStr) == sorted(check)

    l, r, res = 0, len(check)-1, []

    while r < len(original):
        if isSame(original[l:r+1]): res.append(l)
        r+=1
        l+=1

    return res

def subarray_sum_longest(nums: List[int], target: int) -> int:
    left = max_win_len = win_len = 0
    right = 1
    win_sum = nums[left] + nums[right]

    while right < len(nums):
        if win_sum < target:
            # only extend window rightward
            right += 1
            # update window sum
            win_sum += nums[right]

        elif win_sum == target:
            # Compare with previous max length
            win_len = (right-left) + 1
            max_win_len = max(win_len, max_win_len)

            # update window sum and move forward
            win_sum -= nums[left]
            left += 1
            
            right += 1
            # check that right is still within the bounds of the array
            if right >= len(nums): return max_win_len 
            win_sum += nums[right]

        else:
            # update window sum and move forward
            win_sum -= nums[left]
            left += 1

            right += 1
            # check that right is still within the bounds of the array
            if right >= len(nums): return max_win_len
            win_sum += nums[right]
    return max_win_len

def longest_substring_without_repeating_characters(s: str) -> int:
    longest_substr = left = right = 0
    unique_chars = {}

    while right < len(s):
        if s[right] in unique_chars:
            # sequence broken, char is no longer unique. Check if that sequence was the longest seen so far
            longest_substr = max(longest_substr, len(unique_chars))

            # move window forward. Left should move to the value after the duplicate character
            left = unique_chars[s[right]] + 1
            right = left

            # cleanup. Reset unique character set
            unique_chars.clear()
        else:
            # character is unique. Add to set
            unique_chars[s[right]] = right

            # Check if the sequence is the longest seen so far
            longest_substr = max(longest_substr, len(unique_chars))

            # keep finding more unique characters by expanding window
            right += 1

    return longest_substr

#arr: 1 -20 -3 30 5 4 target: 7
def subarray_sum(arr: List[int], target: int) -> List[int]:
    left, right = 0, 1
    sub_sum = arr[left] + arr[right]
    res = []

    while right <= len(arr):
        if sub_sum == target: 
            # result gotten. Return early
            res.append(left)
            res.append(right + 1)
            return res
        elif sub_sum < target:
            # only move right when sub array sum is less than target
            right += 1

            # assert that right pointer is within array bounds before accessing value
            if right >= len(arr): return res
            sub_sum += arr[right]
        else:            
            # when subarray sum is greater than target, don't stop expanding the window. A negative-positive combo might exist ahead
            # for example -1,-1, 5, -1 and target 2
            right += 1

            # end of array. We are now certain that no combo exists for the subarray window
            # shrink window: 
            # 1. by deducting the value at left pointer and move left pointer forward
            if right == len(arr) - 1:
                sub_sum -= arr[left]
                left += 1

                # 2. and move right pointer to just a step ahead of left pointer
                right = left + 1

                # with a new window, we need to recalculate window sum afresh and discard old sum
                sub_sum = arr[left] + arr[right]
            if right > len(arr): return res
    return res


















move_zeros([1,1,2,0,4,4,6,0,1])
two_sum_sorted(sorted([1,1,2,0,4,4,6,0,1]), 5)
is_palindrome('Was it a car or a cat I sawt?')
subarray_sum_fixed([1,1,2,0,4,4,6,0,1], 3)
subarray_sum_longest([1, 6, 3, 1, 2, 4, 5], 10)
longest_substring_without_repeating_characters('abcdbea')
print(subarray_sum([1, -20, -3, 30, 5, 4], 7))