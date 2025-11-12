#print the numbers from 1 to n and count,sum and average the numbers
i=1;c=0;s=0
n=int(input("Enter the number:"))
while(i<=n):
    print(i,end="")
    c=c+1
    s=s+i
    i=i+1
print()    
print("Count=",c)
print("Sum=",s)
print("Average=",(s/c))