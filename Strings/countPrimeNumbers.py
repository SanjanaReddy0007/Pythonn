
n = int(input())

p_count = 0

for num in range(2,n):
    is_prime = True

    for i in range(2 , num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        p_count += 1

print(p_count)

