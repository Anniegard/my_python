x = input('Введите число ')
summ = 0
for i in range(len(x)):
    if int(x[i]) % 2 == 1:
        summ += int(x[i])*int(x[i])
print("ответ: ", summ)
