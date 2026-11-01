S = input()
word = ""
first = "Z"
last = "a"

for i  in range(len(S)):
    char = S[i]
    if char != " ":
        word += char

    if char == " " or  i == len(S) - 1:
        if word.lower() < first.lower():
            first = word
        if word.lower() > last.lower():
            last = word
        word = ""

result = first + " "+last
print(result)

