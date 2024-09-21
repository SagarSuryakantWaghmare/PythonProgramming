# f=open('update.txt','r')
# # print(f)
# text=f.read()
# print(text)
# f.close()
#reading to file
# f=open('update.txt2','r')#rt is used when we want to open the file as text and for binary we use rb
# # print(f)
# text=f.read()
# print(text)
# f.close()
# #writing a file
# f=open('update.txt','w')#rt is used when we want to open the file as text and for binary we use rb
# # print(f)
# f.write('Hello ,Guys!')
# #Adding or appened
# f=open('update.txt','a')

# f.write('Hello ,Guys!')
# f.close()
 
with open('update.txt','a') as f:
    f.write("Ok I am inside")