
N = int(input())

for i in range(1 , N + 1):
    star = ( N + 1) - i
    space = (" ") * (i - 1)
    star = str(star)

    print(space + star)



