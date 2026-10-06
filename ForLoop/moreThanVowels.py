S = input()
vowel = "aeiou"

count = 0

for char in S:
    if(char == vowel):
        count += 1

if count > 2:
    print("IT HAS A MORE THAN 2 VOWELS")
else:
    print("NOT AT ALL.....")

