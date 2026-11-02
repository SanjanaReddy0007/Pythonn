
S = input()
S = list(S)

left = 0
right = len(S) - 1

while left < right:
    if not S[left].isalpha():
        left += 1
    elif not S[right].isalpha():
        right -= 1
    else:
        s[left] , s[right] = s[right] , s[left]
        left += 1
        right -= 1
print(''.join(S))


