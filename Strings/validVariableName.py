
word = input()
valid = True

for i in word:
    code = ord(i)
    valid = (65 <= code and code <= 90) or (97 <= code and code <= 122) or (48 <= code and code <= 57)

   if not valid:
      valid = False
      break

print(valid)
