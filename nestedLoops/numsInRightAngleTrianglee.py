
n = int(input())
for row in range(1 , n + 1):
    each = ""
    for col in range(1 , row + 1):
        each = each + str(col) + " "
    for col in range(1, row):
        each = each + str(col) + " "
    print(each)

