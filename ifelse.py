a=['1','2','hello','world']
for i in a:
    if i.isnumeric():
        print(f'number is {i} integer')
    else:
        print(f'word is {i} string')
        
