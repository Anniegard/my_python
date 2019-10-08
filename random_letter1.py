import random
s=['самовар','весна','лето']
a=random.randint(0,(len(s)-1))
b=random.randint(0,(len(s[a])-1))
c=list(str(s[a]))
pr=c[b]
c[b]='?'
print(''.join(c))
q=input("Введите букву: ")
if q:
    if q==pr:
        print('Победа')
    else:
        print('Увы,попробуйте в другой раз')
print('Слово:',s[a])
