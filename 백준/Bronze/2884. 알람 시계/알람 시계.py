H, M = map(int, input().split(' '))

if M - 45 < 0:
    M = 60 - (abs(M-45))
    if H-1 >= 0:
        H = H-1
    else:
        H = H-1+24
else:
    M = M - 45
print(H, M)