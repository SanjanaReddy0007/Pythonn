N = int(input())
new_list = []

for i in range(N):
    value = input()
    new_list += [value]

for i in range(N):
    print(new_list[N - i - 1])

