def solution(array):
    cnt = []
    # r_array = sorted(array, reverse=True)
    u_cnt = sorted(list(set(array)))
    
    for i in u_cnt:
            cnt.append(array.count(i))
            
    if len(array) == 1:
        return (array[0])
    elif len(u_cnt) == 1:
        return (array[0])
    elif sorted(cnt)[-1] == sorted(cnt)[-2]:
        return (-1)
    else:
        return (u_cnt[cnt.index(max(cnt))])