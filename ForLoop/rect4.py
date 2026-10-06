M = int(input())
N = int(input())

for i range(1 , M + 1):
    if(i == 1 or i == M):
        print("* " * N)
    else:
        space = " " * (N - 2)
        print("* " + space + "* ")

