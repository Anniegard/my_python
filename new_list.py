from math import sqrt
a=[2,4,9,16,25]

#1
res=[]
for x in range(len(a)):
    res.append(sqrt(a[x]))
    print(res)

#2
print(list(map(lambda x: sqrt(x),a)))

#3
print{[sqrt(x) for x in a]}
