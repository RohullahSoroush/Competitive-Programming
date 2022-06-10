# uva 11679
while True:
    b, n = map(int, input().split())
    if b+n ==0:
        break                              #b: bank number    n: debenture number
    r = list(map(int, input().split()))    #r: bank reserves
    flag = True
    for j in range(n):
        d, c, v = list(map(int, input().split()))
        r[d-1] -= v                         #d: بدهکار  #c:طلبکاز    #v:مقدار قرضه
        r[c-1] += v
    for i in r:
        if i<0:
            flag = False
            break
    if flag:
        print("S")
    else:
        print("N")