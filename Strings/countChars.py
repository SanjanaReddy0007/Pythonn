
word = input()
N = int(input())

count = 0

for i in word:
    if(N == ord(i)):
        count = count + 1
    
print(count)
