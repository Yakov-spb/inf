# lesson 3 hw
a = int(input())
if a > 100:
    user_id = 100
    b = [range( a + 1)]
    sum = 0
    for i in b:
     sum += i**3
    print(sum)
else:
     print ("предел не более 100")

#lesson 3/2
n = int(input('введите максимальное число '))
for i in range(1, 7):
    print(i, 'x', n, '=', i * n, )
    
# lesson 3/3
b = input().split
c = rotate (b)
print (c)