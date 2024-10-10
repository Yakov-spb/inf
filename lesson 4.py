a = 'ель нос если'
a = ' ' + a
k = 0
for i in range(len(a)-1):
    #c = a.find("е")
    if a[i:i+2] == ' е':#шаг в 2 символа
        k+=1
print(k)

