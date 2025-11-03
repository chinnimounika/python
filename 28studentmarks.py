#Student Marks
Sno=int(input("Enter Student Number:"))
Sname=input("Enter Student Name:")
Sclass=int(input("Enter Student Class:"))
Ssec=input("Enter Student Section:")
m1=int(input("Enter M1 Marks:"))
m2=int(input("Enter M2 Marks:"))
m3=int(input("Enter M3 Marks:"))
m4=int(input("Enter M4 Marks:"))
m5=int(input("Enter M5 Marks:"))
m6=int(input("Enter M6 Marks:"))
tot=m1+m2+m3+m4+m5+m6
avg=tot/6
print("___________________________________________")
print("MARKS REPORT")
print("____________________________________________")
print("Sno=",Sno,"\t","Sname=",Sname)
print("Sclass=",Sclass,"\t","Ssec=",Ssec)
print("____________________________________________")
print("M1=",m1,"\t","M2=",m2)
print("M3=",m3,"\t","M4=",m4)
print("M5=",m5,"\t","M6=",m6)
print("_____________________________________________")
print("Total Marks=",tot)
print("Percentage of Marks=",avg)
print("______________________________________________")
if(m1<35 or m2<35 or m3<35 or m4<35 or m5<35 or m6<35):
    print("Fail")
elif(avg>=60):
    print("Grade A")
elif(avg<60 and avg>=45):
    print("Grade B")
elif(avg<45):
    print("Grade C")