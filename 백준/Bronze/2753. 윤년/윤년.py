a = int(input()) # 1 < a < 4000

y4 = [] # 4배수
y100 = [] # 100배수
y400 = [] # 400배수

for i in range(1, 4001):
    if i % 4 == 0:
        y4.append(i)
    if i % 100 == 0:
        y100.append(i)
    if i % 400 == 0:
        y400.append(i)

y = list(set(y4) - set(y100))
y1 = list(set(y) | set(y400))

if a in y1:
    print(1)
else:
    print(0)