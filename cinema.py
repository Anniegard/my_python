# cinema.py
name = input("Выбрать фильм; ")
day = input("Выбрать день(сегодня, завтра): ")
time = int(input("Выбрать время: "))
col = int(input("Выбрать количество билетов: "))
print("Выбрали фильм: ", name, " День: ", day, " Время: ", time, " Количество билетов: ", str(col))
k = 0
if name == "Пятница":
    if time == 12:
        cost = col * 250
    elif time == 16:
        cost = col * 350
    elif time == 20:
        cost = col * 450
    else:
        print("Ошибка ввода.")
        k=1
elif name == "Чемпионы":
    if time == 10:
        cost = col * 250
    elif time == 13:
        cost = col * 350
    elif time == 16:
        cost = col * 350
    else:
        print("Ошибка ввода.")
        k=1
elif name == "Пернатая банда":
    if time == 10:
        cost = col * 350
    elif time == 14:
        cost = col * 450
    elif time == 18:
        cost = col * 450
    else:
        print("Ошибка ввода.")
        k=1
else:
    print("Ошибка ввода.")
    k=1
if col >= 20:
    cost = cost * 0.8
if day == "завтра":
    cost = cost * 0.95
elif day != "сегодня":
    print("Ошибка ввода.")
    k=1
if k == 0:
    print("Результат: ", cost)
