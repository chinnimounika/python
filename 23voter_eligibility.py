#Voter Eligibility
age=int(input("Enter your age:"))
if(age>=65):
    print("Senior Citizen")
    print("Eligible to Vote")
elif(age<65 and age>=18):
    print("Major Citizen")
    print("Eligible to Vote")
elif(age<18):
    print("Minor Citizen")
    print("Not Eligible to Vote")