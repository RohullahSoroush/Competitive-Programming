# uva_11364
tc = int(input())
for i in range(tc):
    store_num = int(input())
    m = list(map(int, input().split()))
    m.sort()
    # at firts sort the list and (last-first)
    # because it is the minimal distance
    # *2 the result because of goin and coming back again
    res = abs(m[0] - (m[store_num - 1]))
    print(res*2)