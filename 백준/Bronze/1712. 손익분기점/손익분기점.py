A, B, C = map(int, input().split())
X = 1
if B > C or B == C:
    point = -1
elif C > B :
    point = int((A/(C-B))+1)
print(point)