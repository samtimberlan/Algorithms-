from collections import Counter



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result, lookup, slow, fast, anagram = [], {}, 0, 1, []

        # Have a lookup dict
        # Use two pointers. Fast and slow
        # Slow controls loop
        # Fast checks each element
        # If match, add both to result and lookup
        # Move Slow to next element, provided it is not in lookup
        # Reset Fast to index of next element after Slow

        if len(strs) < 2:
            result.append(strs)
            return result

        while slow < len(strs):

            # if len(strs) == 1:
            #     return result.append(strs)
            
            if fast < len(strs) and Counter(strs[slow]) == Counter(strs[fast]):
                anagram.append(strs[fast])
                lookup[strs[slow]] = slow
                lookup[strs[fast]] = fast
                strs.pop(fast)
            else:
                fast += 1

            # End reached. Reset
            if (fast >= len(strs) or slow + 1 > len(strs)):
                anagram.insert(0, strs[slow])
                result.append(anagram)
                anagram = []

                if slow + 1 < len(strs) and strs[slow + 1] in lookup:
                    slow += 2
                    fast = slow + 1
                else:
                    slow += 1
                    fast = slow + 1
                

        return result
    
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     result, lookup, slow, fast, anagram, reduction_dict = [], {}, 0, 1, [], {}

    #     # Have a lookup dict
    #     # Use two pointers. Fast and slow
    #     # Slow controls loop
    #     # Fast checks each element
    #     # If match, add both to result and lookup
    #     # Move Slow to next element, provided it is not in lookup
    #     # Reset Fast to index of next element after Slow
    #     reduction_dict = {k:k for k,v in enumerate(strs)}

    #     while slow < len(strs):

    #         if len(strs) == 1:
    #             return result.append(strs)
            
    #         if fast < len(strs) and Counter(strs[slow]) == Counter(strs[fast]):
    #             if fast in reduction_dict:
    #                 anagram.append(strs[fast])
    #                 lookup[strs[slow]] = slow
    #                 lookup[strs[fast]] = fast
    #                 del reduction_dict[slow]
    #                 del reduction_dict[fast]
    #         fast += 1

    #         # End reached. Reset
    #         if (fast > len(strs) or slow + 1 > len(strs)):
    #             anagram.insert(0, strs[slow])
    #             result.append(anagram)
                
    #             anagram = []

    #             slow += 1
                

    #     return result


strs = ["eat","tea","tan","ate","nat","bat"]   
sol_obj = Solution()
print(sol_obj.groupAnagrams(strs=strs))
print(sol_obj.groupAnagrams(strs=["a","a","a","a"]))
print(sol_obj.groupAnagrams(strs=["strs"]))
print(sol_obj.groupAnagrams(strs=[""]))
