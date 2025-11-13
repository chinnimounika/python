#Program to print numbers from 1 to 10, their count,sum and average
c=0;s=0
for i in range(1,11):
    print(i)
    c=c+1
    s=s+i
print("Count=",c) 
print("Sum=",s)
print("Average=",(s/c))   