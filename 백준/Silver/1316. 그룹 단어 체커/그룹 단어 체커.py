t = int(input())
cnt = 0
non = 0
for i in range(t):
    string = input()
    slist = list(string)
    nlist = []
    check = 0
    
    for i in slist:
        nlist.append(slist.index(i))
        
    if len(set(string)) == 1:
        cnt += 1
        continue
    else:
        for i in nlist:
            re = 1
            if check <= i:
                check = i
                re += 1
            elif check > i:
                non += 1
                break
            # else:
        # if re == len(set(string)):
        #     cnt += 1
print(t-non)