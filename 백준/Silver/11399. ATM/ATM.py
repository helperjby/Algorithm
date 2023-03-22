n = int(input())
p = list(map(int, input().split( )))

# 리스트의 정렬
p = sorted(p)
t = 0
suml = []

for i in p:
    t += i
    suml.append(t)

print(sum(suml))