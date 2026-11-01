
numm = float(input())
N = int(input())

for i in range(1, N + 1):
    res = numm * i
    term += res
print(round(term, 4))

