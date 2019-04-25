long_string = input('') 
short_string = input('') 
result = [] 
shotgun=0 
while long_string: 
    a=long_string.find(short_string) 
    if a==-1: 
        break
    result.append(a+shotgun)
    shotgun+=a+len(short_string)
    long_string=long_string[a+len(short_string):]
print(result)
