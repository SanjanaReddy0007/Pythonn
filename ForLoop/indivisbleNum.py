
N = int(input())
divi = False

for i in range(2 , 10):
    if(n % i) == 0:
        divi = True

if divi:
    print("divisible Number")
else:
    print("InDivisible number....")

