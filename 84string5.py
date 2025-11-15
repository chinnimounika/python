#Finding exact number of characters in a string
c=0
x="State Bank of India"
for i in x:
    if (i==""):
        continue
    c=c+1
print("Number of characters:",c)