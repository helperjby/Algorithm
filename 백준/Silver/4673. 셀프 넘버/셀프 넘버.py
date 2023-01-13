# 10000 미만의 모든 d(n)
a = 0
dn = []
for i in range(10000):
    if i < 10:
        a = i+i
    else:
        a = i+sum(list(map(int, str(i))))
    if i != a and a < 10000:
        dn.append(a)
# 셀프 넘버 출력
for i in range(1, 10000):
    if i not in dn:
        print(i)