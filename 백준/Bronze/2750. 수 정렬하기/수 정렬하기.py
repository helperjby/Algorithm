repeat = int(input())
numlist = []
for i in range(repeat):
    n = int(input())
    numlist.append(n)
    
for j in sorted(numlist):
    print(j)