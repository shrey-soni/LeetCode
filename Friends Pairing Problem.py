# Friends Pairing Problem

def countWaysRecursive(n):
    MOD=1000000007
    if n<=2:
        return n
    else:
        return (countWaysRecursive(n-1)+countWaysRecursive(n-2)*(n-1))%MOD

def countWaysDP(n):
    arr=[-1 for x in range(n+1)]
    MOD=1000000007
    arr[0]=0
    for i in range(1,n+1):
        if i<=2:
            arr[i]=i
        else:
            arr[i]=(arr[i-1]+arr[i-2]*(i-1))%MOD
    return arr[n]

def countWays(n):
    if n<=2:
        return n
    b,c=1,2
    for x in range(3,n+1):
        new = (c+b*(x-1))%1000000007
        b=c
        c=new
    return c

print(countWaysRecursive(15))
print(countWaysDP(15))
print(countWays(15))