
n = int(input())

for i in range(0,n):
    star = "* " * (n - i)
    space = (" ") * (2 * i)
    print(star + space + star)

for i in range(1 , n + 1):
    star = ("* ") * i
    space = (" ") *(2 *(n - i))
    print(star + space + star)

