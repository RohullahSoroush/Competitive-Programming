n, m = list(map(int, input().split()))
from heapq import _siftdown
# from queue import PriorityQueue
from collections import deque
for _ in range(n):
    data = list(map(int ,input().split()))
    k = int(input())  #number of sorted in leftside or rightside
    data = deque(data)
    data.rotate(abs(k-len(data)))
    data = list(data)
    print(*data)
