N = int(input())
g = list(map(int, input().split(' ')))
m = 0
for i in g:
    m += (i/max(g)) * 100
print(m/N)