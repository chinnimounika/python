#Converting list to tuple,set,frozen set
x=[56,466,678,44,67,78,53,67,78,90,54]
print(x)
print(type(x))
a=tuple(x)
print(a)
print(type(a))
b=set(x)
print(b)
print(type(b))
c=frozenset(x)
print(c)
print(type(c))
