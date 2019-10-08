# call_tel.py
code = float(input("Введите код города; "))
time = float(input("Введите количество минут: "))

if code:
    if time:
        if code == 343:
            cost = 15
        elif code == 381:
            cost = 18
        elif code == 473:
            cost = 13
        elif code == 485:
            cost = 11
        money = cost * time
        print(money)
    else:
        print("Введите время!")
else:
    print("Введите код города!")
