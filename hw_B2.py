1st variant

a=input(' ')
a=(a.replace('T', 'a').replace('C','g').replace('G', 'c').replace('A', 't').upper()[::-1])
print(a)


2nd variant

s = input(' ') 
print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))
