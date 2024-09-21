#for the printing the 5 table by break
for i in range(12):
    if(i==10):
        break
    print("5 X",i+1,"=",5*(i+1))
print("Exit loop")
# printing by the continue statement
for i in range(12):
    if(i==11):
        print("Exit loop")
        break
    elif(i==10):
        print("Skip the iteration")
        continue
    else:
        print("5 X",i+1,'=',5*(i+1))
