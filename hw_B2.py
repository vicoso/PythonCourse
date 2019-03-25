a=input(' ')
a=(a.replace('T', 'a').replace('C','g').replace('G', 'c').replace('A', 't').upper()[::-1])
print(a)
