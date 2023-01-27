T = int(input())

for i in range(T):
    room = ''
    H, W, N = map(int, input().split()) 
    # 1 1 1
    # 2 2 2
    # 40 50 200
    # 6 12 10
    # 30 50 72 
    # 10 10 100
    # 층 구하기
    if N <= H:
        floor = N
    elif N % H == 0:
        floor = H
    else:
        floor = N % H
    # print(floor)
    # 방 배정하기
    if N <= H:
        number = 1
    elif N % H == 0:
        number = N//H
    else:
        number = (N // H)+1
    # print(number)
    if number > 9:
        room = str(floor)+str(number)
    else:
        room = str(floor) + '0' +str(number)
    print(int(room))