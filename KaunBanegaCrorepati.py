print("Kaun Banega Crorepati")
a=input("What is your Good Name:")
import time
t=time.strftime("%H,%M,%S")
hour=int(time.strftime("%H"))
if(hour>=0 and hour<12):
    print("Good Morning ",a)
elif(hour>=12 and hour<15):
    print("Good Afternoon ",a)
else:
    print("Good Night ",a)
print("Welcome to the KBC,So we shall start now")  
listq=["1.Which of the following is Palindrome Number: (1).345 (2).121 (3).3443 (4).2 and 3","1.Which of the following is not the Access modifier in java : (1).public (2).static (3).private (4).default","1.Can we perform the multiple inhertaince in java: (1).NO (2).YES (3).Yes,but only by the interfaces (4).None of these","1.Which of the following is not the inbuilt method in java : (1).Math.max() (2).Array.sort() (3).Array.reverse()(4).Math.min()"]  
for i in listq:
    print(i)
    i=int(input("Enter the  answer :"))
    if(i==4):
        print("You won 100000")
    elif(i==2):
        print("You won  6000000 ")  
    elif(i==3):
        print("You won 36000000")  
    elif(i==3):
        print("You won 7 core") 
    else:
      print("Kya Programmer banegare tu !")   
      break
print("Thank you for participating")
