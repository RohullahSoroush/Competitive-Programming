# uva 11559
while True:
    n, b, h, w = map(int, input().split())
    #n :number of participaint
    #b :budget, bodegah
    #h :number of hotels
    #w :number of weeks ot chosse which week to stay
    ans = 0
    e = False
    for i in range(h):
        p = int(input())  #price for staying in hotel
        week = list(map(int, input().split()))
        if p*n<=b:
            week.sort(reverse=True)
            if week[0] >=n:
                e = True
                if ans ==0:
                    ans = p*n
                elif p*n<ans:
                    ans = p*n
    if e:
        print(ans)
    else:
        print("stay home")


