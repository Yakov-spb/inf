a = 'ананас кегля абстракция'
b= a.split( )
i = 0
while i < len(b):
    if b[i].startswith('а') and b[i].endswith('я'):
        print(b[i])
    i = i+2