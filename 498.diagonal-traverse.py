#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret=[]
        dir=True
        for sum in range(len(mat)+len(mat[0])-1):
            temp=[]
            if sum<=len(mat)-1:
                y,x=0,sum
            else:
                y=sum-len(mat)+1
                x=sum-y
            while x>=0 and y<len(mat[0]):
                temp.append(mat[x][y])
                x-=1
                y+=1
            if not dir:
                temp=temp[::-1]
            for x in temp:
                ret.append(x)
            dir = not dir
        return ret
# @lc code=end

