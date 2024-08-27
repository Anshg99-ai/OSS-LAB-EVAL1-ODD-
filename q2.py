a=input("enter the string:")
words=a.split()
freq={}
freq1={}
for i in a:
    if i in freq and i!=" ":
        freq[i]=freq[i]+1
    else:
        freq[i]=1
c=-1
for i in a:
    if(freq[i]>c):
        s=i
        c=freq[i]
print(s,"->",c)
for word in words:
    if word in freq1:
         freq1[word]=freq1[word]+1
    else:
        freq1[word]=1
d=-1
for i in words:
    if (freq1[i]>d):
        p=i
        d=freq1[i]
print(p,"->",d)  
 
