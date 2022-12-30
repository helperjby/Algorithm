N = int(input())

count=1
a = N
while True:
    b = ((N%10)*10)+(((N//10) + (N%10))%10)
    if b != a:
        N = ((N%10)*10)+(((N//10) + (N%10))%10)
        count = count+1
    else:
        print(count)
        break