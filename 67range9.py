#program to print numbers from 1 to n,their count,sum and average
s=0;c=0
n=int(input("Enter the Number:"))
for i in range(1,n+1):
    print(i)
    c=c+1
    s=s+i
print("count=",c)
print("sum=",s)
print("Average=",(s/c))    