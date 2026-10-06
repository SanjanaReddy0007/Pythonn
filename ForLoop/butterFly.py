
N = int(input())

for i in range(1, N + 1):
    star = ("* ") * i
    space = (" ") * (2 * (n - 1))
    print(star + space + star)

for i in range(1 , n):
    star = ("* ") * (n - i)
    space = (" ") * (2 * i)
    print(star + space + star)

