n = int(input())
for _ in range(n):

    m = int(input())
    temp = int(input())
    data = list(map(int, input().split()))
#first line the testcase:
    res = []
    for i in data:
        for j in data:
            if i+j == m:
                if not [i,j] in res:
                    res.append([i,j])

    for i in res:
        print(*i)