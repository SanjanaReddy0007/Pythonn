S=input()
first=S 
word=""

for i in range(len(S)):
    char=S[i]
    word+=char
    
    if char==" " or i==len(S)-1:
        if word.lower()<first.lower():
            first=word
        word=""
print(first)



