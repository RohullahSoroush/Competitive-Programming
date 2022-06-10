n = int(input())
for _ in range(n):
    m = int(input())
    data = input().split(",")
    n = 0
    for i in data:
        if len(i) > n:
            n = len(i)
    res = []
    for i in data:
        if len(i)==n:
            res.append(i)
    # res = list(sorted(res))
    print(*res)