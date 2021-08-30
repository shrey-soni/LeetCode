#
# @lc app=leetcode id=1784 lang=python3
#
# [1784] Check if Binary String Has at Most One Segment of Ones
#

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if "01" in s:
            return False
        else:
            return True
# @lc code=end

obj=Solution()
print(obj.checkOnesSegment("11"))

