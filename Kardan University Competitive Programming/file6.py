n = int(input())
import string
for _ in range(n):
    data = input()
    res = []
    temp = list(string.ascii_uppercase)+list(string.ascii_lowercase)
    for i in range(len(data)):
        res.append(temp[temp.index(data[i])+1])


    print("".join(res))