i=1;c=0;s=0;ce=0;se=0;co=0;so=0
while(i<=5):
    print(i,end="")
    c=c+1
    s=s+i
    if(i%2==0):
        ce=ce+1
        se=se+i
    else:
        co=co+1
        so=so+i
    i=i+1
print()
print("Count of All=",c)
print("Sum of All=",s)
print("Average of All=",(s/c))
print("________________________________")
print("Count of Even=",ce) 
print("Sum of Even=",se) 
print("Average of Even=",(se/ce))
print("_________________________________")
print("Count of Odd=",co) 
print("Sum of Odd=",so) 
print("Average of Odd=",(so/co))
print("__________________________________")    