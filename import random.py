import random

n = [[(random.randint(1, 9)), (random.randint(1, 9)),( random.randint(1, 9)) ], [(random.randint(1, 9)), (random.randint(1, 9)), (random.randint(1, 9)) ], [(random.randint(1, 9)), (random.randint(1, 9)), (random.randint(1, 9))]]

print('матрица 1 ')
for i in n:
  print(' '.join(list(map(str, i))))
a= list()
a.extend(n[1])
print(a)
l = max(a)
print (l)
b=list()
for i in n:
  b.append(i[2])
  print(b)
g = max(b) 
print (g)