N = int(input())
small = 999999999

for i in range(N):
    num = int(input())
    if num < small:
        small = num
    
print(small)
    