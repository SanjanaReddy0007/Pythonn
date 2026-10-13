N = int(input())
M = int(input())
K = M * N

for i in range(M):
    for j in range(N):
        print(K,end = " ")
        K -= 1
    print()

