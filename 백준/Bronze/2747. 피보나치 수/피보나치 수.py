n = int(input())
start = [0, 1]

if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n > 1:
    for i in range(n-1):
        start.append(start[-1] + start[-2])
    print(start[-1])