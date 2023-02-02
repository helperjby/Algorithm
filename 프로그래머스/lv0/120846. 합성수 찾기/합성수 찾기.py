def solution(n):
    num2 = []
    num3 = []
    num5 = []
    num7 = []

    for i in range(2, (n//2)+1):
        num2.append(i*2)
    for i in range(2, (n//3)+1):
        num3.append(i*3)
    for i in range(2, (n//5)+1):
        num5.append(i*5)
    for i in range(2, (n//7)+1):
        num7.append(i*7)

    fprime = list(set(num2+num3+num5+num7))
    return len(fprime)