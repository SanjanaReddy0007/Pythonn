box = list(map(int,input().split()))
low = 0
mid = 0
high = len(box) - 1

while mid <= high:
    if box[mid] == 0:
        box[low] , box[mid] = box[mid] , box[low]
        low += 1
        mid += 1
    elif box[mid] == 1:
        mid += 1
    else:
        box[mid],box[high] = box[high] , box[mid]
        high -= 1

print(*box)


