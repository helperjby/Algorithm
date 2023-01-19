T = int(input())
for i in range(T):
    r, s = map(str, input().split())
    p = ''
    for j in s:
        p += j*int(r)
    print(*p, sep='')
