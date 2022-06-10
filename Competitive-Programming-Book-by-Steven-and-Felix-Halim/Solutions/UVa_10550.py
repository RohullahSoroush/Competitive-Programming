# uva_10550
while True:
    line = list(map(int, input().split()))
    if line[0]==0 and line[1]==0 and line[2]==0 and line[3]==0:
        break
    degree = 0
    degree += 720
    degree += ((line[0] - line[1]) + 40)*9
    degree += 360
    degree += ((line[2] - line[1]) + 40)*9
    degree += ((line[2] - line[3]) + 40)*9
    print(degree)
