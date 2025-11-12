#print the numbers from 1 to n and sum the numbers
i=1;s=0
n=int(input("Enter the number:"))
while(i<=n):
    print(i,end="")
    s=s+i
    i=i+1
print("Sum=",s)