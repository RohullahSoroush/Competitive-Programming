# uva 11547
while True:
    tc = int(input())
    for i in range(tc):
        n = int(input())
        res = int(((((((n*567)/9) + 7492)*235)/47) - 498))
        res = str(res)
        print(res[-2])
