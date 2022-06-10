# uva_11332
while True:
    n = int(input())
    if n == 0:
        break
    n = str(n)
    while (len(n)>1):
        m = sum(int(i) for i in n)
        n = str(m)
    print(n)



