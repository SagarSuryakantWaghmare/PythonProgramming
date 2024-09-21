#basic purpose of the generators is it's faster
#it only generates not store the values in the memory
def my_generators():
    for i in range(101):
        yield i
gen=my_generators()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#By the for loop 
for j in gen:
    print(j)