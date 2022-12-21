ch, cm = map(int, input().split(' '))
pm = int(input())

pm_a = pm//60
pm_b = pm%60

if cm + pm_b >= 60:
    m = abs(60 - (cm + pm_b))
    if ch + pm_a + 1 > 23:
        h = ch + pm_a + 1 - 24
    else:
        h = ch + pm_a + 1
else:
    m = cm + pm_b
    if ch + pm_a > 23:
        h = ch + pm_a - 24
    else:
        h = ch + pm_a
        
print(h, m)