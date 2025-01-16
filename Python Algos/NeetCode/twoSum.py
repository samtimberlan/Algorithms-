def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        comps = {}
        for k,v in enumerate(nums):
            comp = target - v

            if comp in comps:
                return [comps[comp], k]
            else:
                comps[comp] = k

def twoSumS(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lookup = {}
        for key, value in enumerate(nums):
            diff = target - value
            if diff in lookup:
                return [lookup[diff], key]
            else:
                lookup[value] = key


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
print(twoSumS(nums, target))