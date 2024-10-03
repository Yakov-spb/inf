#lesson 3 homework
a = int(input())
if a > 100:
    user_id = 100
    b = [range(1, a + 1)]
    sum = 0
    for i in b:
        sum += i**3
        print(sum)
else:
    print("предел не более 100")