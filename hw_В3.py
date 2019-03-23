a=input(' ')
b=input(' ')
a==b
s=0
for i in range(len(a)):
    if a[i]!=b[i]:
        s+=1
        print(s)
