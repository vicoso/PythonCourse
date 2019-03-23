a=input(' ')
b=(a.replace('T', 'H'), a.replace('C','P'))
c=(b.replace('A', 'T'), b.replace('G','C'))
f=(c.replace('H', 'A'), c.replace('P','G'))
reversed_f=f[::-1]
print(reversed_f)
