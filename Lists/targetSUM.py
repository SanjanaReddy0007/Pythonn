N = list(map(int,input().split()))
target = int(input())

found = False
for i in range(len(N)):
    for j in range(i + 1, len(N)):
        if N[i] + N[j] == target:
            print(i,j)
            found = True
            break
    
    if found:
        break
        
