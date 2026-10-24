
n = int(input())
for i in range(1 , n + 1):
    if(i > 2 and i < n):
        hollow = (" ")*(n - i)
        nums = "1 " + hollow + (str(i) + " ")
        print(nums)
    else:
        nums = ""
        for j in range(1, i + 1):
            nums = nums + (str(j)) + " "
        print(nums)
        
