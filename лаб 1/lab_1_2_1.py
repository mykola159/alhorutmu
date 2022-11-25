#from lab_1_1 import *


class Node:

	
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None



def inorder(root):
	if root is not None:
		inorder(root.left)
		print (root.key,end=" ")
		inorder(root.right)


# ф-я для вставки
def insert(node, key):

	
	if node is None:
		return Node(key)

	# рекурсія
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	
	return node

#мінімальний елемент


def minValueNode(node):
	current = node

	# пошук найбільш лівого елемента
	while(current.left is not None):
		current = current.left

	return current

# ф-я видалення


def deleteNode(root, key):

	
	if root is None:
		return root

	
	if key < root.key:
		root.left = deleteNode(root.left, key)

	
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	
	else:

		# дерево без нащадків
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# з двома нащадками
		temp = minValueNode(root.right)

		
		root.key = temp.key

		
		root.right = deleteNode(root.right, temp.key)

	return root
def minimum(root):
        if root==None:
            return float('+inf')
        else:
            res=root.key
            lres=minimum(root.left)
            rres=minimum(root.right)
            if lres<res:
                res=lres
            if rres<res:
                res=rres
        return res
def tree_successor(root):
    if root.right!=None:
        return minimum(root.right)
    y=root.parent
    while(y!=None and x==y.right):
        x=y
        y=y.parent
    return y.key
def search_node(root,data):#пошук елементу
        if data < root.key:
            if root.left is None:
                print(data," not found")
                root=search_node(root.left,data)
            print(root.key,' is found ')
        elif data > root.key:
            if root.right is None:
               print(data," not found")
               root=search_node(root.right,data)
            print(root.key,' is found ')
        else:
            print(root.key," is found!")
# діаграма
""" Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """

'''root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print ("Inorder traversal of the given tree")
inorder(root)

print ("\nDelete 20")
root = deleteNode(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 30")
root = deleteNode(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal of the modified tree")

'''
root=None

while(True):
        x=int(input('Choose option\n1) Insert\n2) delete\n3) search\n4) successor node\n5) show tree\n'))
        if x==0:
                root = insert(root, 50)
                root = insert(root, 30)
                root = insert(root, 20)
                root = insert(root, 40)
                root = insert(root, 70)
                root = insert(root, 60)
                root = insert(root, 80)
                inorder(root)

        elif x==1:
                a=int(input('Put for insert '))
                root=insert(root,a)
                print('\n\n\n')
                inorder(root)
                print(' -> ')
        elif x==2:
                a=int(input("element for delete "))
                root=deleteNode(root,a)
                print('\n\n\n')
                inorder(root)
                print(' -> ')
        elif x==3:
                a=int(input('Put for insert '))
                root=search_node(root,a)
                print('\n\n\n')
                inorder(root)
                print(' -> ')
        elif x==4:
                print(tree_successor(root))
