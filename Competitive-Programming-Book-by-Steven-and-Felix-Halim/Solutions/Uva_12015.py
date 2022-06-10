# uva_12015
n = int(input())
j = 0
while n>0:
    str = []
    temp = 0
    for i in range(10):
        lucky = input().split()
        url = lucky[0]
        value = int(lucky[1])
        if value > temp:
            str = [url]
            temp = value
        elif value == temp:
            str.append([url])
    j+=1
    print("Case #{}:".format(j))
    print(*str, sep="\n")
