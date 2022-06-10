# uva_10300
n = int(input())                                        #n: testcases
while n>0:
    f = int(input())                                    #f: number of farmers
    temp = 0
    for i in range(f):
        s, a, m = list(map(int, input().split()))       #s: farmyard size
        animal_space = s/a                              #a: number of animals
        premium = (animal_space*m)                      #m: farmers environment friendliness
        result = (premium*a)
        temp += result
    print(int(temp))
    n-=1