
N = int(input())
total = 0

for i in range(1, n):
    if(N % i) == 0:
        total += i

if total == N:
    print("Perfect Number")
else:
    print("Not a Perfect Number...")

