# for i in range(6):
#     print(i)
# else:
#     print("Sorry for this ",i+1)    
# for i in[]:
#     print(i)
# else:
#     print("Sorry no i")        
# for i in []:
#     print(i)
#     if i==4:
#         break
# else:
#     print("Sorry no i")    
for i in range(6):
    print(i)
    if i==4:
        break    
else:
    print("Sorry no i")
#If the for loop is executed and there is break then the else part is not executed
i=0
while i<5:
    print(i)   
    i=i+1
else:
    print("sorry for i")    
#for the format
for x in range(5):
    print("iteration no {} in for loop".format(x+1))   
else:
    print("Out of loop")        