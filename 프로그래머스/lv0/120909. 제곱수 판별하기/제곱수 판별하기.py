def solution(n):
    n_list = []
    for i in range(1, 1001):
        n_list.append(i**2)
    if n in n_list:
        return 1
    else:
        return 2
    # for i in range(1, 1001):
    #     if n == i**2:
    #         return 1
    #     else:
    #         return 2