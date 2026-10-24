
s = input()

first_char = 0

for char in s:
    if(char == " "):
        break
    else:
        first_char = first_char + 1

first_index = s[:first_char]
upp = first_index.upper()
whole = upp + s[first_char: ]

print(whole)
