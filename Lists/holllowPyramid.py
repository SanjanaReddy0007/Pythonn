
N = int(input())

for i in range(N):
    if i == 0:
        each = "|"
    else:
        space = " "*i
        each = "|" + space + "/"
    print(each)


for i in range(N):
    if i == n - 1:
        each = "|"
    else:
        space = " "*(N - i - 1)
        each = "|" + space + "\"
    print(each)
    
 
