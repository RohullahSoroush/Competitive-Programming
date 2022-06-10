# uva_11799
t = int(input())
for i in range(t):
    line = list(map(int, input().split()))
    n = line[0]
    line.pop(0)
    line = sorted(line)
    print("Case {0}: {1}".format(i+1,max(line)))
