#time module is used to get time for the specific work
import time
# def usingFor():
    
#     for i in range(1000):
#         print(i)
# def usingWhile():
#     i=0
#     while i<1000:
#         i=i+1
#         print(i)  
# init=time.time()                 

# usingFor()
# t1=time.time()-init
# init=time.time()
# usingWhile()
# t2=time.time()-init
# print("THE Time requried for Using For loop t1:",t1)
# print("The time requried for Using While loop:",t2)
# print(4)
# time.sleep(4)
# print("This printed after the 4 second")
#for the local time
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d  %H-%M-%S",t)
print(formatted_time)
# OUtput for this is:2024-01-28  17-10-06