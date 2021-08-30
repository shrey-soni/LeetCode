 #
# @lc app=leetcode id=1774 lang=python3
#
# [1774] Closest Dessert Cost
#

# @lc code=start
def closestNum(target,b,c):
    if abs(target-b) > abs(target-c):
        return c
    else:
        return b

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        closest=float('inf')
        def recurse(toppingCosts,i,used,target,costSoFar):
            if costSoFar==target:
                return costSoFar
            if used>2:
                return recurse(toppingCosts,i+1,0,target,costSoFar)
            if i==len(toppingCosts):
                return costSoFar
            else:
                if toppingCosts[i]<=target:
                    return closestNum(target,recurse(toppingCosts,i+1,0,target,costSoFar),recurse(toppingCosts,i,used+1,target,costSoFar+toppingCosts[i]))
                else:
                    return recurse(toppingCosts,i+1,0,target,costSoFar)
            return None
        for x in range(len(baseCosts)):
            closest=closestNum(target,closest,recurse(toppingCosts,0,0,target,baseCosts[x]))
        return closest
        # def recurse():
        #     return None

        # return recurse()
# @lc code=end

