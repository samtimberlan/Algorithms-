class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD':400, 'CM':900}
        norm = 0
        l, r = 0, 1
        
        # II
        while l < len(s):
            rom = s[l]
            if r < len(s):
                next_rom = s[r]
            else:
                next_rom = s[l]
            
            if r < len(s) and rom == 'I' and next_rom == 'V' or rom == 'I' and next_rom == 'X':
                sub = rom + next_rom
                if sub in nums:
                    norm += nums[sub]
                l+=2
                r+=2
            elif r < len(s) and rom == 'X' and next_rom == 'L' or rom == 'X' and next_rom == 'C':
                sub = rom + next_rom
                if sub in nums:
                    norm += nums[sub]
                l+=2
                r+=2
            elif r < len(s) and rom == 'C' and next_rom == 'D' or rom == 'C' and next_rom == 'M':
                sub = rom + next_rom
                if sub in nums:
                    norm += nums[sub]
                l+=2
                r+=2
            else:
                if rom in nums:
                    norm += nums[rom] 
                l+=1
                r+=1
                
        return norm
    

s = "LVIII"
s2 = 'IV'
s3 = 'I'
sol = Solution()
print(sol.romanToInt(s))
print(sol.romanToInt(s2))
print(sol.romanToInt(s3))
