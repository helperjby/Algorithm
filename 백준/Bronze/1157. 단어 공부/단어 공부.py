string = sorted(str(input()).upper())
u_string = list(set(string))
cnt_n = []
for i in u_string:
    cnt_n.append(string.count(i))

if len(cnt_n) == 1:
    print(*string) 
elif sorted(cnt_n)[-2] == sorted(cnt_n)[-1]:
    print('?')
else:
    print(u_string[cnt_n.index(max(cnt_n))])