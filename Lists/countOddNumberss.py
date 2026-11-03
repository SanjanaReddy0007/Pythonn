
Low = int(input())
High = int(input())

count = 0

for i in range(Low , High + 1):
    if i % 2 == 1:
        count += 1 

print(count)


