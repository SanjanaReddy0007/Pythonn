N = list(map(int, input().split()))
index = 0

for i in range(len(N)):
    if N != 0:
        N[index] = N[i]
        index += 1

for i in range(index , len(N)):
    N[i] = 0

print(*N)

