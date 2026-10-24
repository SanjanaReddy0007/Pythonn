
n = int(input())
for row in range(1 , n + 1):
    each_row = ""
    for col in range(1, n + 1):
        if row == 1 or row == n:
            each_row = each_row + str(col)
        else :
            if col == 1 or col == n:
                each_row = each_row + str(col)
            else :
                each_row = each_row + " "
    print(each_row)

# 1 2 3 4
# 1     4
# 1     4
# 1 2 3 4 for n = 4.................

