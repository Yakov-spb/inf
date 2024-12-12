a = 'ананас кегля абстракция'
b= a.split( )
for i in b:
    if i.startswith('а') and i.endswith('я'):
        print(i)
