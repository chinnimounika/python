#Count the number of digits in a given number
i=1;c=0
n=int(input("Enter the number:"))
while(i<=n):
    n=n/10
    c=c+1
print("count=",c)  