M = int(input())
N = int(input())
count = 0

for i in range(M ,  N + 1):
    if(i % 6) == 0:
        count += 1
    divi = divi + str(i)

if count == 0:
    print("Not")
else:
    print(divi)

