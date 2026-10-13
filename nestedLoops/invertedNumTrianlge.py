num = int(input())
for i in range(num):
    each = ""
    numm = num - i
    for j in range(1 , numm + 1):
        each = each + str(j) + " "
    print(each)

