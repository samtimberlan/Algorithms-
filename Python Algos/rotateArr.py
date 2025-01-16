def rotLeft(a, d):
    # Write your code here
    lookup = {}
    res = []
    
    for i in range(d):
        if i - 1 in lookup:
            res = lookup[i-1]
            num = res.pop(0)
            res.append(num)
        else:
            num = a.pop(0)
            a.append(num)
            lookup[i] = a
            res = a
    return res

print(rotLeft([1, 2, 3, 4], 3))