class Solution(object):
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            slow, fast = 0, 1
            lookup = {
                "{": "}",
                "(": ")",
                "[": "]"
            }


            while fast < len(s):
                if s[slow] not in lookup:
                    return False
                elif s[slow] in lookup and lookup[s[slow]] != s[fast]:
                    return False

                slow += 2
                fast = slow + 1
            return True

s = "()[]{}" 
sol_obj = Solution()
print(sol_obj.isValid(s=s))