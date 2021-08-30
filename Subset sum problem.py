# Subset sum problem

def subsetsum(arr):
    s=sum(arr)
    if s%2!=0:
        return False
    h={}
    def recurse(target,i,arr):
        if i>=len(arr):
            return False
        if target==0 and i<=len(arr)-1:
            return True
        if (i,target) in h.keys():
            return h[(i,target)]
        if arr[i]<=target:
            h[(i,target)]=recurse(target-arr[i],i+1,arr) or recurse(target,i+1,arr)
            return h[(i,target)]
        else:
            h[(i,target)]= recurse(target,i+1,arr)
            return h[(i,target)]
    return recurse(s//2,0,arr)

print(subsetsum([1,5,3]))