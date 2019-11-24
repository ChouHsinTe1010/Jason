class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val:
            if root.val >= val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)

            else:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)

        else:
            root.val=val
            return root


        '''if root.val is None:
                root.val=val
            elif root.val > val:
                if root.left is None
                    root.left = TreeNode(val)
                else:
                    self.insert(root.left, val)
            elif root.val < val:
                if root.right is None
                    root.right=TreeNode(val)
                else:
                    self.insert(root.right, val)
            else:
                temp = TreeNode(val)
                temp.left=root.left
                root.left=temp'''

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if  root is None:
            return root
        if root.val > target:
            root.left=self.delete(root.left, target)
        elif root.val < target:
            root.right=self.delete(root.right, target)
        else:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            temp_val=root.right
            mini=temp_val.val
            while temp_val.left:
                temp_val=temp_val.left
                mini=temp_val.val
            root.val=mini
            root.right=self.delete(root.right,root.val)
            if root is not None:
                Solution().delete(tmp, target)
        return root

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root:
            if root.val is target:
                return root
            if root.left:
                temp=self.search(root.left, target)
                if temp is not None:
                    return temp
            if root.right:
                return self.search(root.right, target)


    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        cnt=[0]
        def dfs_cnt(root, target):
            if root:
                if root.val == target:
                    cnt[0] = cnt[0]+1
                dfs_cnt(root.left, target)
                dfs_cnt(root.right, target)
        dfs_cnt(root, target)
        self.delete(root, target)
        for i in range(cnt[0]):
            self.insert(root, new_val)
            return root
        '''sort_array=list()
            def traverseInorder(root, target):
                if root:
                    traverseInorder(root.left, target)
                    sort_array.append(root.val)
                    traverseInorder(root.right, target)
            def insertBalanced(start ,end):
                if(start>end):
                    return None
                mid = (start + end) // 2
                node=TreeNode(sort_array[mid])
                node.left = insertBalanced(start, mid-1)
                node.right = insertBalanced(mid+1, end)
            traverseInorder(root, target)
            insertBalanced(0, len(sort_array)-1)
            tree2D = self.printTree(node)
            for i in range(len(tree2D)):
                for j in range(len(tree2D[i])):
                    if tree2D[i][j]=="":
                        print(" ", end='')
                    else:
                        print(tree2D[i][j], end='')
                print("")'''


    '''def printTree(self, root):
        def height(root):
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1

        def fill(root, h, l, r):
            if not root: return
            mid = (l + r) // 2
            m[h][mid] = str(root.val)
            if root.left: fill(root.left, h + 1, l, mid - 1)
            if root.right: fill(root.right, h + 1, mid + 1, r)

        h = height(root)
        w = 2 ** h - 1
        m = [[""] * w for _ in range(h)]
        fill(root, 0, 0, w - 1)
        return m


tmp=TreeNode(5)
Solution().insert(tmp, 3)
Solution().insert(tmp, 3)
Solution().insert(tmp, -5)
Solution().insert(tmp, 8)
Solution().insert(tmp, 7)
Solution().insert(tmp, 6)
Solution().insert(tmp, 10)
print(Solution().insert(tmp,4)==tmp.left.right)

Solution().delete(tmp, 3)
print(tmp.val == 5 and tmp.left.val == -5 and tmp.left.left == None and tmp.left.right == None)
print(tmp.right.right.val== 10 and tmp.right.left.val == 7 and tmp.right.left.left.val == 6)
print(tmp.right.right.right== None and tmp.right.right.left == None and tmp.right.left.right == None)
print(tmp.right.left.left.left== None and tmp.right.left.left.right == None and tmp.right.val == 8)

print(Solution().search(tmp,10) == tmp.right.right)


Solution().modify(tmp, 7, 4)
tree2D=Solution().printTree(tmp)
#print(tree2D)

tree2D=Solution().printTree(tmp)
#print(tree2D)
for i in range(len(tree2D)):
    for j in range(len(tree2D[i])):
        if tree2D[i][j]=="":
            print(" ", end='')
        else:
            print(tree2D[i][j], end='')
    print("")
'''
