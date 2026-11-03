N = list(map(int,input().split()))

even = [x for x in N if x %  2 == 0]
odd = [x for x in N if x % 2 != 0]

print(even + odd)

