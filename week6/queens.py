def attack(r1,c1,r2,c2):
    if r1==r2: return True
    if c1==c2: return True 
    if abs(r1-r2)==abs(c1-c2): return True

    return False

N = 15

def queens1(col,rows_used):
    if col==N:
        for i in range(len(rows_used)):
            for j in range(i+1, len(rows_used)):
                if attack(rows_used[i],i, rows_used[j], j):
                    return 0
        return 1
    count = 0
    for row in range(N):
        if row not in rows_used:
            count+=queens1(col+1,rows_used+[row])

    return count 

print(queens1(0,[]))