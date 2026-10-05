
N = input()
N_len = len(N)
sum = 0

for i in N:
    sum = int(i) ** N_len

if sum == int(n):
    print("Armstrong Number...")
else:
    print("Not an Armstrong Number...")

