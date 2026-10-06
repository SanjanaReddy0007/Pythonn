N = int(input())

for i in range(1 , N + 1):
    star = i
    space = 4 * (n - i)
    print(("* ") * star + (" ") * space + ("* ") * star)

