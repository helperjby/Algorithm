N = int(input())
M = list(map(int, input().split()))

a = sorted(M)
print(a[0], a[-1])