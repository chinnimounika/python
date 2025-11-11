#program to set fore,back,style,import time
from colorama import Fore,Style
import time
i=1
st=time.time()
while(i<=10):
 if(i%2==0):
  time.sleep(2)
  print(Fore.RED,i)
 elif(i%2!=0):
  time.sleep(3)
  print(Fore.BLUE,i)
 i=i+1 # Moved the increment outside the conditional blocks
et=time.time()
print(Style.RESET_ALL)
print("Time Taken=",(et-st))