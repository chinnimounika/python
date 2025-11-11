#program to set Fore and Back color and also rest to oroginal after loop (!pip colorama install) 
from colorama import Back,Fore,Style
i=1
while(i<=5):
 print(Back.YELLOW,Fore.RED,i)
 i=i+1
 print(Style.RESET_ALL)
print("INDIA")