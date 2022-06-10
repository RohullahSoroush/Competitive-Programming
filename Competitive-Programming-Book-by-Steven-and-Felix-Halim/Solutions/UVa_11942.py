# uva_11942
n = int(input())
print("Lumberjacks:")
while n>0:
    numbers = list(map(int, input().split()))
    temp1 = list(numbers)
    temp2 = list(numbers)
    temp1.sort()
    temp2.sort(reverse=True)
    if numbers == temp1 or numbers == temp2:
        print("Ordered")
    else:
        print("Unordered")
    n-=1