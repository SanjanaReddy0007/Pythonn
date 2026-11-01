
N = int(input())

for i in range(1, N + 1):
    zeroes = "0" * (2 * i + 1)
    dot = "." * (N - i - 1)
    print(dot + zeroes + dot)

for i in range(1, N):
    zeroes = "0" * (2 * (N - i) - 1)
    dot = "." * i
    print(dot + zeroes + dot)

