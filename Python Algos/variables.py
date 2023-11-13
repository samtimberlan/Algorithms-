from collections import Counter
import math

a = str(1)
b = "Hello, World!"
c = a + b

d=e=f = "hello"
g,h,i = 1, 2.0, 'world'

j = ["john", "doe"]
k, l = j

m = frozenset({"apple", "banana", "cherry"})
n = {"apple", "banana", "cherry"}
o = {"name" : "John", "age" : 36}
p = ("apple", "banana", "cherry")
q = ["apple", "banana", "cherry"]
r = 1j
s = float('inf')
t = math.inf


txt = "The best things in liFe are free!"

# All string methods return new values. They do not change the original string.

# enumerate function gives access to index and element
for i, word in enumerate(txt.split(' ')): 
    print(i, word)

count = Counter(txt)
print(count)


print(" ")
print("----------")

#slicing
print(b[2:5])
print(b[-5:-2])

print(" ")
print("----------")

print(txt.casefold())
print(txt.encode())

print(" ")
print("----------")

print("expensive" not in txt)
print (c)
print (type(b))
#print(e + i)
#comilation error because of plus sign. print(g+d)
print(g,d) # no compilation error with this format
print(k+l)
print(k,l) # This format adds extra space in between the output

print(type(m))
print(type(n))
print(type(o))
print(type(p))
print(type(q))
print(type(r))
print(type(s))
print(t)


"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""