class Node:
    def __init__(self, value = None, parent = None, child = None):
        self.value = value
        self.parent = parent
        self.child = child
    
class Tree:
    def getParent(self, value):
        return value.parent
    def getChild(self, value):
        return value.child
    def traversing(self, root):
        while root.child is not None:
            print(root.value)
            root = root.child 

x = Tree()
print(x.child)
