
N = int(input())

for i in range(n):
    space = (" ") * (n - i)
    star = ("* ") * ((2 * i) + 1)
    print(space + star)

