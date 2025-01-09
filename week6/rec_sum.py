l = [1,2,3,4,5,6]

def  rec_sum(l):
    print(f"{l[0]=} {l[1:]=}")
    if len(l)==1: 
        return l[0]
    return l[0]+rec_sum(l[1:])

denominations = [1,15,25]
dp = {}
def cc(value, used):
    if value==0: return used 
    
    if value<0: return 1000000000
    if (value, used) in dp: return dp[(value,used)]
    
    min_used = 100000000000
    for coin in denominations:
        min_used=min(min_used,cc(value-coin, used+1))
    
    dp[(value,used)] = min_used
    
    return min_used

print(cc(200,0))