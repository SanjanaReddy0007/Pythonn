M = int(input())
N = int(input())

res = ""

for i in range(M , N + 1):
    if (i % 2) == 1:
        res = res + str(i) + " "

print(res)

