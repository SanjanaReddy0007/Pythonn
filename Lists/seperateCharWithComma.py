
word = input()
res = ""

for i in range(len(word) - 1):
    res += word[i] + ","
res += word[len(word) - 1]
print(res)

