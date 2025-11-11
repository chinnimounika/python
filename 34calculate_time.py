#program to print numbers also calculate time taken
import time
i=1
st=time.time()
while(i<=100000):
 print(i)
 i=i+1
et=time.time()
print("Time Taken=",et-st)