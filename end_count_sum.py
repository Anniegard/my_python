x = input('Введите число ')
summ = 0
while True:
    if x == "stop":
        print("Ответ: ", summ)
        break
    elif x.isdigit():
        summ += int(x)
    else:
        print("Ошибка ввода.")
    x = input("Введите новое число: ")
