# uva_11044
while True:
    tc = int(input())
    for i in range(tc):
        n, m = list(map(int, input().split()))
        result = ((n//3) * (m//3))
        print(result)


