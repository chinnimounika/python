#frozen set
x={"pen","pencil","book","eraser"}
print(x)
print(type(x))
x.add('scale')
print(x)
print(type(x))
print("____________________")
y=frozenset(x)
print(y)
print(type(y))
y.add("Nipuna") #gives error because frozen set cannot be modified
print(y)