
row = int(input())

for i in range(1 , row + 1):
    space = " " * (row - i)
    if i == 1:
        each_row = space + (chr(i + 64) + " ")
    else:
        hollow = (" ") * (i - 2)
        each_row = space + (chr(i + 64)+" ") + hollow + (chr(i + 64) + " ")
    res = " "*(row - i)
    print(each_row + res + each_row)
    

