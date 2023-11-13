class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            
            # Find boundary
            if nums[mid] <= r:
                # Find postition within boundary. Move right
                l = mid - 1
                mid = (l+r) // 2
                if nums[mid] < target:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                # Move left
                r = mid + 1
                mid = (l+r) // 2
                if nums[mid] < target:
                    r = mid -1
                else:
                    l = mid + 1
        return -1
    
sol_obj = Solution()
print(sol_obj.search(nums =[1], target=0))