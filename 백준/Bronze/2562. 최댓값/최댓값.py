a = []
i = 0
while i < 9:
    a.append(int(input()))
    i += 1

print(max(a))
print(int(a.index(max(a)))+1)
        