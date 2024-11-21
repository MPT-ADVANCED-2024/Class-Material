import random, time

def distinct_sorting(x,n):
    x.sort()

    if len(x)==0:
        distinct = 0
    else:
        distinct = 1
        for i in range(1,n):
            if x[i]!=x[i-1]:
                distinct+=1
    return distinct

def distinct_list(x, n):
    distincts = []

    for i in range(n):
        if x[i] not in distincts:
            distincts.append(x[i])
    return len(distincts)

n = 100000000
x = [random.randrange(1,1000) for i in range(n)]

a = time.time()
print(distinct_list(x,n))
b = time.time()
print("Took",round(b-a,3),"seconds")

a = time.time()
print(distinct_sorting(x,n))
b = time.time()
print("Took",round(b-a,3),"seconds")
