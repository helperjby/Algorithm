N = int(input())

for i in range(1, N+1):
    a = '*' * i
    # print('% s'%(N, a))
    # print("{0:>N}".format(a))
    print(a.rjust(N))