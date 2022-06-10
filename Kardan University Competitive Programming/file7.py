data = []
for _ in range(5):
    data.append(list(map(int, input().split())))
    loc = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 1:
            loc = [i+1, j+1]
final = [3,3]
print(loc, final)
print(abs(final[0]-loc[0])+abs(final[1]-loc[1]))

