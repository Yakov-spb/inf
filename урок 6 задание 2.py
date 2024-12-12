n = 3
arr = list()
#Заполняем массив 9-ми
for i in range(n):
  arr.append([9]*n)
#Вывод исходного массива
for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()