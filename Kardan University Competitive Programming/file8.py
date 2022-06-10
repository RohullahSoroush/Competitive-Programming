n = int(input())
data = list(map(int, input().split()))

def Z_sort(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j] and i%2==0:
                data[i], data[j] = data[j], data[i]
            elif data[i] < data[j] and i%2!=0:
                data[i], data[j] = data[j], data[i]
            else:
                print("Impossible")
    return data

# def sol2(data):
#     res = list(sorted(data))
#     res1 = res[0:int(len(data)/2)]
#     res2 = res[int(len(data)/2):]
#     out = []
#     for i in range(len(res1)):
#         out.append(res1[i])
#         out.append(res2[i])
#     return out

print(*Z_sort(data))