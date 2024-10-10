a = 'анннистннвввнн'
k = [_.replace("н", "!") for _ in a]
print(k)

a = 'это задание (домашка) было выполнена'
i = 0
while a[i] != '(':
    i += 1
i += 1
while a[i] != ')':
    print(a[i])
    i += 1    

    a = 'ананас кегля абстракция'
b= a.split( )
i = 0
while i < len(b):
    if b[i].startswith('а') and b[i].endswith('я'):
        print(b[i])
    i = i+2