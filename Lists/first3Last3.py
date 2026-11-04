N = int(input())
list_a = []

for i in range(N):
    value = input()
    list_a += [value]

new_list = list_a[:3] + list_a[N - 3:]
print(new_list)

