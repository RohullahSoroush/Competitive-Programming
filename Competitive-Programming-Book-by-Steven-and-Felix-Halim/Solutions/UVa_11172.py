# uva_11172
tc =  int(input())
while tc < 15:
    i, j = input().split()
    if i > j:
        print(">")
    elif i < j:
        print("<")
    else:
        print("=")