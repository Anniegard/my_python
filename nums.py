x = 'В разные эпохи и у разных народов число\
Пи имело разное значение. Например,\
в Древнем Египте оно равнялось 3.1604 \
у индусов оно приобрело значение 3.162 \
китайцы пользовались числом, равным 3.1459 \
Буквенное обозначение число Пи получило только \
в 1706 году – оно происходит от начальных букв \
двух греческих слов, означающих окружность и \
периметр. Буквой π число наделил математик Джонс,\
а прочно вошла в математику она уже в 1737 году.'
k=0
answer = []
transfer = ''
for i in range(len(x)):
    s = x[i]
    if k == 0:
        if s.isdigit():
            k = 1
            transfer += s
    else:
        if s != ' ':
            transfer += s
        else:
            k = 0
            try:
                int(transfer)
            except Exception:
                answer += [float(transfer)]
            else:
                answer += [int(transfer)]
            transfer = ''
            
print(answer)
print(len(answer))
print(max(answer))
            
            
