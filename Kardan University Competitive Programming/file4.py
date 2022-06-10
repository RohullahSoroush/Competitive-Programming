n,m = list(map(int, input().split()))
import math
for _ in range(n):
    if _!=0:
        m = int(input())
    data = list(map(int, input().split(",")))
    ans = -9999999
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i]*data[j]>=ans and i!=j and (i+1==j or i-1==j):
                ans = data[i]*data[j]
    print("Case #"+str(_+1)+";",ans)

    # ‎2
    # 6
    # ‎3, 6, -2, -5, 7, 3
    # ‎7
    # ‎7, -2, 19, -1, 3, 8, 10‎

