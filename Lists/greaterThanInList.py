L = [1, 20, 33, 45, 520, 64, 71, 852, 9999, 101010]

N = int(input())
new_list = []

for i in L:
    if i > N:
        new_list += [i]

print(new_list)



