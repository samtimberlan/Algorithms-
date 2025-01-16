def reverseVowels(s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        vowel_idxs = set()
        stack = []
        s_arr = list(s)
        
        for i, v in enumerate(s_arr):
            if v in vowels:
                stack.append(v)
                vowel_idxs.add(i)
            else:
                continue
        
        
        for idx in vowel_idxs:
            vowel = stack.pop(-1)
            s_arr[idx] = vowel
            
        return ''.join(s_arr)

print(reverseVowels("race a car"))