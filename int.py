a, b = input().split()
a, b = map(int, (a, b))
if b !=0:
    c = a/b
    print('результат деления',c)
else:
        print("делить на ноль нельзя!")