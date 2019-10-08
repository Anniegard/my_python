x = 'Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог'
k=0
answer = ' '
for i in range(len(x)):
    if k == 0:
        if x[i]=='м' and x[i-1] == ' ':
            k = 1
        else:
            answer += x[i]
    else:
        if x[i] == ' ':
            k = 0
print(answer)
            
            
