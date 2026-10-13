
n = int(input())
for i in range(1 , n):
    for j in range(i + 1, n):
        k = n - i - j
        if j < k <= n:
            count += 1
print(count)

