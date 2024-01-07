deepestPath = ""
depth = 1
deepestValue = ""

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
    def deepestBranch(self):
        findDeepest(self)
        print("Depth of the tree:", depth)
        print("Path to the deepest node:", deepestPath)
        print("Value of the deepest node:", deepestValue)
        
def printPreorder(node):
    if node:
        print("-->",node.val, end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

def printInorder(node):
    if node:
        printInorder(node.left)
        print("-->",node.val, end=" ")
        printInorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print("-->",node.val, end=" ")
        
def insertSort(node,val):
    if node is None:
        return Node(val)
    else:
        if node.val is val:
            return node
        elif node.val < val:
            node.right = insertSort(node.right, val)
        else:
            node.left = insertSort(node.left, val)
    return node

def findDeepest(node, type = 'root', currentDepth = 0, currentPath="root"):
    global deepestPath, depth, deepestValue

    if node:
        currentDepth += 1
        if type == 'left':
            currentPath += ".left"
        if type == 'right':
            currentPath += ".right"
        findDeepest(node.left, 'left', currentDepth, currentPath)

        if currentDepth > depth:
            depth = currentDepth
            deepestPath = currentPath
            deepestValue = node.val

        findDeepest(node.right, 'right', currentDepth, currentPath)
        
# Implemented an internal function deepestBranch() which calls the external function findDeepest and print the result.
# depth, deepestPath and deepestValue are global variables
# node, type (root/left/right), currentpath, currentdepth is the parameters

# # Task5b and 5c
# root = Node('Haziman Sairin')
# insertSort(root,'Zikri Hakim')
# insertSort(root,'Jameel Majdi')
# insertSort(root,'Raniya Waleed')
# insertSort(root,'Syukri Talib')
# insertSort(root,'Izzat Syahmi')
# insertSort(root,'Saif al-Din')
# insertSort(root,'Nuqman Aliff')
# insertSort(root,'Amir Su\'ad')
# insertSort(root,'Abdul Karim')
# insertSort(root,'Kamarul Danial')
# insertSort(root,'Dania Izzah')
# insertSort(root,'Fariz Yazid')
# insertSort(root,'Zharif Aiman')
# insertSort(root,'Sharifa Harun')
# insertSort(root,'Fuad Najma')
# insertSort(root,'Muhd Fakhrul')
# print("Preorder")
# printPreorder(root)
# print('\n')
# print("Inorder")
# printInorder(root)
# print('\n')
# print("Postorder")
# printPostorder(root)
# print('\n')
# print("Deepest Branch")
# root.deepestBranch()
