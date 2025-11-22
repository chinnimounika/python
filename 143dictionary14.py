#Combining 2 dict
x={1:"a",2:"b",3:"c"}
y={4:"d",5:"e",6:"f"}
print(x)
print(y)
z={**x,          **y}
print(z)
print("____________________")
x.update(y)
print(x)