
class BTree(object):
    def __init__(self, val=None):
        self.val= val
        self.right = None
        self.left = None
        self.hd= 0
    def printTree(self, root, space=0, LEVEL_SPACE=5):
        if root == None:
            return
        space += LEVEL_SPACE
        self.printTree(root.right, space)
        for i in range(LEVEL_SPACE, space):
            print(end=" ")
        print("|" + str(root.val) + "|")
        self.printTree(root.left, space)
    
    def print_tree(self, traversal_type):
        if traversal_type=="preorder":
            return self.preorder_print(root, "")
        elif traversal_type=="inorder":
            return self.inorder_print(root, "")
        elif traversal_type=="postorder":
            return self.postorder_print(root, "")
        else:
            print("Traversal type"+ str(traversal_type)+"is not supported")
            return False  
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.val) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.val) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.val) + "-")
        return traversal

root=BTree(1)
root.left=BTree(2)
root.right=BTree(3)
root.left.left=BTree(4)
root.left.right=BTree(5)
root.right.left=BTree(6)
root.right.right=BTree(7)
root.right.right.right=BTree(8)

while(True):
    print("Choose your option")
    print("1 to show tree, 2 to sort with preorder, 3 to sort with inorder, 4 to sort with postorder")
    a=int(input())
    if a==1:
        root.printTree(root)
    if a==2:
        print(root.print_tree("preorder"))
    if a==3:
        print(root.print_tree("inorder"))
    if a==2:
        print(root.print_tree("postorder"))



    












