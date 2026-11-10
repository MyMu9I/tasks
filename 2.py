lys = [2, 5, 8, 11, 14, 18, 21, 25, 30]
val = 18
first = 0
last = len(lys) - 1
index = -1
while (first <= last) and (index == -1):
    mid = (first + last) // 2
    if lys[mid] == val:
        index = mid
    else:
        if val < lys[mid]:
            last = mid - 1
        else:
            first = mid + 1
print(index)
