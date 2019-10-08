cinema = {
    'Пятница': {'time_price': {12: 250, 16: 350, 20: 450}, 'genre': 'комедия', 'limit': 16},
    'Чемпионы': {'time_price': {10: 250, 13: 350, 16: 350}, 'genre': 'спорт', 'limit': 16},
    'Пернатая банда': {'time_price': {10: 350, 14: 450, 18: 450}, 'genre': 'мультфильм', 'limit': 6}
    }
name = input('Выбрать фильм: ')
day = input('Выбрать день (сегодня, завтра): ')
time = input('Выбрать время: ')
col = input('Выбрать количество билетов: ')
k = 0
price = 0
print('Вы выбрали фильм: ', name,' День: ', day, ' Время: ', time, ' Количество билетов: ', col)
if name in cinema and int(time) in cinema[name]['time_price']:
    price = cinema[name]['time_price'][int(time)]
else:
    k = 1
if col.isdigit():
    price *= int(col)
    if int(col) >= 20:
        price *= 0.8
else:
    k = 1
if day == 'завтра':
    price *= 0.95
elif day != 'сегодня' :
    k = 1
if k == 1:
    print('Ошибка ввода.')
else:
    print('Стоимость бмлетов: ', price)
