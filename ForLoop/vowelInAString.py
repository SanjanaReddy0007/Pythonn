
s = input()
vowel = ""

for char in s:
    vowels = "aeiou"
    if char in vowels:
        vowel += char

print(vowel)

