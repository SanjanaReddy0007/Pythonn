S = input()

if len(S) == 0:
    print(-1)
else:
    first_uniq = -1

    for char in S:
        if S.count(char) == 1:
            first_uniq = char
            break
    print(first_uniq)
    

