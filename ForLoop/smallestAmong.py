N = int(input())
first = int(input())

for i in range(1 , N - 1):
    num = int(input())
    if num < first:
        first = num

print(first)

