#Program to print the numbers,squares and cube upto n numbers
n=int(input("Enter a Number:"))
print("Number \t Square \t Cube")
print("________________________________")
for i in range(1,n+1):
    print(i,"\t",i*i,"\t",i*i*i)
    