todo = []
while True:
    a = int(input('Простой todo;\n \t 1. Добавить задачу.\n \t 2. Вывести список задач.\n \t 3. Выход.\n\nУкажите число: '))
    if a == 1:
        task = input('Введите задачу: ')
        category = input('Введите категорию задачи: ')
        time = input('Введите время к задаче: ')
        todo += [{'task':task,'category':category,'time':time}]
    if a == 2:
        for i in todo:
            print('Задача: ',i['task'],' Категория: ',i['category'],' Время: ', i['time'])
    if a == 3:
        break
