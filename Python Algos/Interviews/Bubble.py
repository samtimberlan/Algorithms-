
print("Hello, world!")

    0    1    2    3    4
0# 1    1    1    1    1
1# 1    2    3    4    5
2# 1    3    6   10   15
3# 1    4    10  20   35
4# 1    5    15  35   70

matrix(2,2)
range (2,2)

base row = rt 1
base column = rt 1

check if first row set 1
Store value in hashmap with r,c as keys
To compute next value look up r,c in hashmap

`${row},${col}`

left r[c-1] 1,1: 2
top r-1[c] 2,0: 1

def matrix(r,c):
    curr = 0
    res = {}
    for row in range(r):
        for col in range(c):
            if row == 0:
                curr = 1
                res[$`{row},${col}`] = curr
            elif col == 0:
                curr = 1
                res[$`{row},${col}`] = curr
            else:
                top = $'{row-1},{col}'
                left = $`{row},{col-1}`
                top_val = res[top]
                left_val = res[left]
                curr = top_val + left_val
                res[$`{row},${col}`] = curr