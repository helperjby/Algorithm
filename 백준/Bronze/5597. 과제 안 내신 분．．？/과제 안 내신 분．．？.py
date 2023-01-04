a = []
b = []

for i in range(28):
    b.append(int(input()))
    
for i in range(1, 31):
    a.append(i)
    if i not in b:
        print(i)
