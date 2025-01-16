def minAddToMakeValid(s: str) -> int:
        ans, open_brackets = 0, 0

        # only put opening in stack
        # pop stack if closing found

        for l in s:
            if l == "(":
                open_brackets += 1

            # matched
            else:
                if open_brackets > 0: open_brackets -= 1
                else:
                    ans += 1

        return ans + open_brackets

s = "((("      
print(minAddToMakeValid(s))