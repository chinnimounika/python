#print the numbers from 1 to n and count the numbers
i=1;c=0
n=int(input("Enter the number:"))
while(i<=n):
    print(i,end="")
    c=c+1
    i=i+1
print("Count=",c)