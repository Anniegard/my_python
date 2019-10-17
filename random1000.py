L =[-123,124,1-124,124,12345,-16245634573,2,-3,4,5,-7,6678899,134,521]
mi=min(L)
ma=max(L)
min_index = L.index(mi)
max_index = L.index(ma)
answer = 0
if min_index<max_index:
    while min_index != max_index:
        if L[min_index] < 0:
            answer += 1
        min_index += 1
else:
    while max_index != min_index:
        if L[max_index] < 0:
            answer += 1
        max_index += 1
print(answer)
