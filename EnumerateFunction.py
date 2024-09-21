marks=[12,3,67,86,100,43,54,6,74]
index=0
for mark in marks:
    print(mark)
    if(index==4):
        print("sagar,Awesome!")
    index+=1   
    # Using the enumerate function
for index,mark in enumerate(marks):
    print(mark)
    if(index==4):
        print("sagar,Awesome!")
         