# write a python program to translate a message into secret code language.Use the rules
# below to translate normal english into secret code language.
'''
Coding:
if the word contains atleast 3 characters,remove the first letter and
append it at the last.
now append three random characters at the starting and the end 
else:
simply reverse the string

Decoding:
if the word contains less than 3 characters,reverse it
else:
removes 3 random characters from the start and end.Now remove the last
letter and append it to the beginning
'''


# print("Welcome to the secret code")
st=input("Enter your Message :")
words=st.split(" ")
coding=input("1 for coding or 0 for Decoding:")
# coding=False#for the decoding
# coding=True#for the coding
coding==True if (coding=="1")else False
if(coding):
    nwords=[]
    for word in words:
      if(len(word)>=3):
        r1="sha"
        r2="agh"
        stnew=r1+word[1:]+word[0]+r2
        nwords.append(stnew)
      else:
         nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
      if(len(word)>=3):
       
        stnew=word[3:-3]
        stnew=stnew[-1]+stnew[:-1]
        
        nwords.append(stnew)
      else:
         nwords.append(word[::-1])
    print(" ".join(nwords))

