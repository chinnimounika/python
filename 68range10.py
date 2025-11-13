import time
c=0;s=0
n=int(input("Enter a Number:"))
st=time.time()
for i in range(1,n+1):
    time.sleep(2)
    print(i)
    c=c+1
    s=s+i
et=time.time()
print("Count=",c)
print("Sum=",s) 
print("Average=",(s/c))
print("Time taken=",(et-st))   