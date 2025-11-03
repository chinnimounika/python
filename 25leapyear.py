#Check Leap Year or not
year=int(input("Enter Year:"))
if(year%400==0):
    print("Leap Year")
elif(year%100==0):
    print("Not a Leap Year")
elif(year%4==0):
    print("Leap Year")
else:
    print("Not a Leap Year")