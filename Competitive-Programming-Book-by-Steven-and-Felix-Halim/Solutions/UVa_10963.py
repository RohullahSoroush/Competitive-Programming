# uva_10963
tc = int(input())
for i in range(tc):
    blank_line = input()
    col = int(input())
    flag = True
    s = 0
    for j in range(col):
        x, y = map(int, input().split())
        if s == 0:
            s = x-y
        elif s != (x-y):
            flag = False
    if flag:
        print()
        print("yes")
    else:
        print()
        print("no")

