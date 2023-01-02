N = int(input())
a = []
a.append(input().split(' '))
b = [data for inner_list in a for data in inner_list]
v = (input())

print(b.count(v))