
m = int(input())
n = int(input())

num = 1
for row in range(m):
    each = ""
    for col in range(n):
        each = each + str(col)
        num = num + 1
    print(each)

