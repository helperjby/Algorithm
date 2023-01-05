C = int(input())
for i in range(C):
    N = list(map(int, input().split()))
    N1 = N[0]
    del N[0]
    avg1 = float(sum(N)/len(N))
    check = []
    for j in N:
        if j > avg1:
            check.append(j)
    solution = len(check)/len(N) * 100
    print("%0.3f%%" % solution)