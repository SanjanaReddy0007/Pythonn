
M=int(input())
N=int(input())
great=max(M,N)
while True:
    if great%M==0 and great%N==0:
        LCM=great
        break
    great+=1 
print(LCM)

