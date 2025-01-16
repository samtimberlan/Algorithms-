def sum_odds(idx, arr: list):
    arr_len = len(arr)
    if idx >= arr_len: return 0
    
    curr = arr[idx]

    if curr % 2 == 0: return sum_odds(idx+1, arr) + 0
    else: return sum_odds(idx+1, arr) + curr

def prd(arr):
    prd = prd_evens(0, arr)

    # No even in list
    if prd == None: return 0
    else: return prd    

def prd_evens(idx, arr: list):
    arr_len = len(arr)
    if idx >= arr_len: return None
    
    curr = arr[idx]
    prd = prd_evens(idx+1, arr)

    if curr % 2 != 0:
        return prd
    if prd == None:
        return arr[idx]
    return arr[idx] * prd


def rec_rev(s):
    return rec_rev_prv(0, s)

def rec_rev_prv(idx, s):
    if idx >= len(s):
        return ''
    return rec_rev_prv(idx+1, s) + s[idx]

def rec_rev_dnq(s):
    return rec_rev_dnq_prv(s)

def rec_rev_dnq_prv(s):
    n = len(s)
    if n <= 1:
        return s
    left,right,rem = s[0], s[n-1], s[1:-1]

    return right + rec_rev_dnq_prv(rem) + left

def ispalindrome_dnq(s):
    return ispalindrome_dnq_prv(s)

def ispalindrome_dnq_prv(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]: return False
    return ispalindrome_dnq_prv(s[1:-1])

def find_max(lst):
    return find_max_prv(0,lst)

def find_max_prv(idx, lst):
    if idx >= len(lst):
        return [float('-inf'), float('-inf')]
    
    res = find_max_prv(idx+1, lst)
    if lst[idx] > res[0]: res = [lst[idx], idx]
    return res

def decimal_to_binary(num):
    if num <= 0:
        return ''
    rem, binary_num = num // 2, num % 2
    return decimal_to_binary(rem) + str(binary_num)

def combinations(lst):
    if len(lst) == 0:
        return [[]]
    curr = lst[0]

    combs_without_curr = combinations(lst[1:])
    combs_with_curr = []

    for comb in combs_without_curr:
        comb_with_curr = comb.append(curr)
        combs_with_curr.append(comb_with_curr)
    return [combs_without_curr, combs_with_curr]


def combinations_2(lst):
    if len(lst) == 0:
        return [[]]
    
    combos = []

    for combo in combinations_2(lst[1:]):
        combos += [combo, combo + [lst[0]]]
    
    return combos



arr = [2,5,4,7,3]
#s = 'slowy'
s = 'abc'

print('sum_odds', sum_odds(0, arr))
print('prd_evens', prd_evens(0, arr))
print('rec_rev', rec_rev(s))
print('rec_rev_dnq', rec_rev_dnq(s))
print('ispalindrome_dnq_prv', ispalindrome_dnq_prv(s))
print('find_max', find_max(arr))
print('decimal_to_binary', decimal_to_binary(233))
print('combinations', combinations(list(s)))
print('combinations', combinations_2(list(s)))
