
X = int(input())
N = int(input())

power = 0
for i in range(1 , N + 1):
    power = power + 2
    term = X ** power

    is_negative = (i % 2) == 0
    if is_negative:
        term = term * (-1)
    sum += term

print(sum)

