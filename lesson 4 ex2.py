a = ('прпгпп:ваапп')
a = ' ' + a
for i in range(len(a)):
    if a[i:i+2] == ':':
        a.replace('%')
        print (a)