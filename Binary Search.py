# Binary Search
def binarySearch(left,right,arr,target):
    mid=(left+right)//2
    if (arr[mid]==target):
        return mid
    elif arr[mid]>target:
        right=mid-1
    elif arr[mid]<target:
        left=mid+1
    return binarySearch(left,right,arr,target)

print(binarySearch(0,9,[1,2,3,4,5,6,7,8,9,10],8))