n = int(input())
x = list(map(int, input().split()))

x.sort()
# y = sorted(x)

if len(x)==0:
    distinct = 0
else:
    distinct = 1
    for i in range(1,n):
        if x[i]!=x[i-1]:
            distinct+=1
print(distinct)

