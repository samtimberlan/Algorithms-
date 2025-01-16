'''
Advantages:
1. Contiguous memory alloc
2. Easy to impl.
3. O(1) access because of Indexing

Disadvantages:
1. O(n) addition and deletion of middle elements
2. Fixed sizing in some languages
'''

def Urlify(n):
    n_arr = list(n.strip())
    for idx, el in enumerate(n_arr):
        if el == " ":
            n_arr[idx] = '%20'
    return ''.join(n_arr)

def Urlify_comp(n):
    return [ el  if el != " " else "%20" for el in n]

print("Urlify", Urlify("Mr   John   Smith "))
print("Urlify2", Urlify("Mr John Smith "))