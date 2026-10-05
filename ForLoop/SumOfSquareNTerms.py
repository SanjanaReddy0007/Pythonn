X = int(input())
N = int(input())

sum = 0

for i in range(1, N + 1):
    term = str(X) * i
    sq = int(term) ** 2
    sum += sq

print(sum)


