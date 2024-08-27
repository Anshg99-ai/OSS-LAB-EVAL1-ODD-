a=input("enter the string:")
b=set()
print("the upper case letters are:")
for i in a:
    if(i.isupper()):
     b.add(i)
for i in b:
    print(i)
c=set()
print("the lower case letters are:")
for i in a:
    if(i.islower()):
        c.add(i)
for i in c:
    print(i)
