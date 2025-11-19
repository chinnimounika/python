#Sum and average of elements in a list without using builtin function
x=[10,20,30,40,50]
s=0
c=0
for i in x:
    print(i,end="")
    c=c+1
    s=s+i
    print("Count=",c)
    print("Sum=",s)
    print("Average=",(s/c))