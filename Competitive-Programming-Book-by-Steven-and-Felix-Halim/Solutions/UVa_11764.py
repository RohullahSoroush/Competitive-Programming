# uva_11764
t = int(input())
while t>0:
    for i in range(t):
        high = 0
        low = 0
        n = int(input())
        w = list(map(int, input().split()))
        for j in range(n-1):
            if w[j] < w[j+1]:
                high += 1
            elif w[j] > w[j+1]:
                low +=1
        print("Case {0}: {1} {2}".format(i+1, high, low))
    t-=1
