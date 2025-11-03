#Check Upper/Lower case or others from Keyword
ch=input("Press any key on keyword:")
if(ch>="A" and ch<="Z"):
    print("Upper Case")
elif(ch>="a" and ch<="z"):
    print("Lower Case")
elif(ch>='0' and ch<='9'):
    print("Digit")
else:
    print("Others")