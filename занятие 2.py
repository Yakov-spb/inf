a = input("введите стоимость покупки \n")
a=int(a) 
if  a > 20:
    d = a * 0,35
    b = a - d
    print ("размер скидки",round (d),"стоимость со скидкой",round (b))
else:
    print("скидка не зачтена,итог:",a)
