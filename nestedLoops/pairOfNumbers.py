
n = int(input())
for i in range(1, n + 1):
    j = n - i 
    if i < j <= n:
        count += 1
print(count)

