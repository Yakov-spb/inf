a = input()
if not a.isdigit():
    a=int(a) 
else:
    a=int(a) 
    a > 0 and a < 13
if a==1 or a==2  or a==12:
    print("время года -зима")
else:
    if a==3 or a==4 or a==5:
        print("время года весна")
    else:
        if a==6 or a==7 or a ==8:
            print("время года лето")
        else:
            if a==9 or a==10 or a==11:
                print("время года - осень")
            else:
                print("введите число от 1 до 12 ")
   



