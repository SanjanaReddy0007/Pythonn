
N = int(input())
for num in range(1 , N + 1):
     digits = str(num)
     power = len(digits)
    armstrong_num = sum(int(digit) ** power for digit in digits)

if(armstrong_num == N):
    print("IT is Armstrong Num")
else:
    print("IT's Not an Armstong Number..")

