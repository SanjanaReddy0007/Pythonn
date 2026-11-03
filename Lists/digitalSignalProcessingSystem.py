N = int(input())
count = 0

while N > 0:
    if N % 2 == 1:
        count += 1
    N = N // 2

print(count)

