a = []
b = []
for i in range(10):
# i = 0
# while i < 10:
    num = int(input())
    if num % 42 not in a:
        a.append(num % 42)
    # i+1
print(len(a))
