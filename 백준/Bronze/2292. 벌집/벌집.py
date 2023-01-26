N = int(input())
i=0
sum=0
while True:
    sum += i*6
    i = i+1
    if sum >= N-1:
        break
print(i)