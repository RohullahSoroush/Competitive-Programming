# uva 11727
tc = int(input())
for i in range(1,tc):
    salary = list(map(int, input().split()))
    salary= list(sorted(salary))
    print("Case {0}: {1}".format(i+1,salary[1]))