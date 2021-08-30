# N-ary Tree Level Order Traversal

class Solution:
    def levelOrder(root):
        ret=[]
        if not root:
            return ret
        ret.append([root.val])
        currentLevel=[root]
        nextLevel=[]
        while len(currentLevel)>0:
            node=currentLevel.pop(0)
            for x in range(len(node.children)):
                if node.children[x]:
                    nextLevel.append(node.children[x])
            if len(currentLevel)==0:
                lis=[]
                for x in range(len(nextLevel)):
                    lis.append(nextLevel[x].val)
                nextLevel,currentLevel=currentLevel,nextLevel
                if len(lis)>0:
                    ret.append(lis)
        return ret