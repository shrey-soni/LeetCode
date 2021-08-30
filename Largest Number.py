# Largest Number
import functools
class Solution:
    def largestNumber(self, nums):
        def compare(a,b):
            if int(a+b)<int(b+a):
                return 1
            elif int(a+b)>int(b+a):
                return -1
            else:
                return 0
        lis=[]
        for x in nums:
            lis.append(str(x))
        l=sorted(lis,key=functools.cmp_to_key(compare))
        print(l)
        ans = '0' if l[0] == '0' else ''.join(l)
        return ans