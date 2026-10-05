
num = int(input())
N_str = str(N)
k = len(num)
sum = 0

for i in N_str:
    sum += int(i) ** k

print(sum)

