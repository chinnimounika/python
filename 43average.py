#program to count,sum and average the numbers from 1 to 5
i=1;c=0;s=0
while(i<=5):
    print(i,end="")
    c=c+1
    s=s+i
    i=i+1
print()
print("\n Count=",c)
print("\n Sum=",s)
print("\n Average=",(s/c))