start = [29, 10, 14, 37, 13]
unsort = start
sort = []
while len(unsort) > 0:
    min = unsort[0]
    for i in range(0, len(unsort)):
        if unsort[i] < min:
            min = unsort[i]
    sort.append(min)
    unsort.remove(min)
    print(sort)
print(sort)
