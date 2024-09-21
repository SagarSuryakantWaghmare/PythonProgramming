import time
t=time.strftime('%H:%M:%S')
# print(t)
# t=int(time.strftime('%H'))
# print(t)
# t=time.strftime('%M')
# print(t)
# t=time.strftime('%S')
# print(t)
hour=int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sagar") 
elif(hour>=12 and hour<17):
    print("Good Afternoon Sagar")
if(hour>=17 and hour<0):
    print("Good Night Sagar")    
