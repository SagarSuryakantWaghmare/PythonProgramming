#seek-to move the current position 
# with open('update.txt','r') as f:
#     print(type(f))
#     f.seek(10)
#     data= f.read(5)
#     print(data)
# with open ('sample.txt','r') as f:
#     print(type(f))
#     data=f.read(10)
#     print(f.tell())#to tell the current position of the data
#truncate
with open('sample2.txt','w') as f:
    f.write('Hello Sagar')
    f.truncate(5)#to write only the first five characters
with open('sample2.txt','r') as f:
    print(f.read())
   
   