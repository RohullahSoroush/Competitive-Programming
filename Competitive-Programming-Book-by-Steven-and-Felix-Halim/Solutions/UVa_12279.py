# uva_12279
tc = int(input())
a =0
while tc!=0:
    for i in range(tc):
        a+=1
        line = list(map(int, input().split()))
        m=0
        n=0
        for j in line:
            if j==0:
                m+=1
            if j>=1 and j<=99:
                m+=1
        emoogle_balance = n-m
        print("Case {0}: {1}".format(a, emoogle_balance))

#
# 5
# 3 4 0 0 1
# 4
# 2 0 0 0
# 7
# 1 2 3 4 5 0 0
# 0