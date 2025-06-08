

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right



class Solution:
    def sameTree( self, p: TreeNode, q:TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
    

def buildTree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue= [root]
    i=1

    while i<len(nodes):
        current= queue.pop(0)
        if i<len(nodes) and nodes[i] is not None:
            current.left= TreeNode(nodes[i])
            queue.append(current.left)
        i+=1
        if i<len(nodes) and nodes[i] is not None:
            current.right= TreeNode(nodes[i])
            queue.append(current.right)
        i+=1
    return root



p = buildTree([1, 2, 3 ])
q = buildTree([1, 2, 3])

sol = Solution()
result = sol.sameTree(p, q)

print(result)

