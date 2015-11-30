__author__ = 'Andy'


class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.value = val

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


class BinaryTree:
    def __init__(self, node=None):
        self.node = node

    def getNode(self):
        return self.node

    def getLeftChild(self):
        return self.node.left

    def getRightChild(self):
        return self.node.right

    def insertNode(self, value):
        if (self.node is None):
            self.node = Node(value)
        else:
            self.addChild(value, self.node)

    def addChild(self, value, node):
        if value < node.getValue():
            if node.left is None:
                node.left = Node(value)
            else:
                self.addChild(value, node.left)
        elif value > node.getValue():
            if node.right is None:
                node.right = Node(value)
            else:
                self.addChild(value, node.right)

    def getMin(self, node=None):
        if node is None:
            node = self.node
        if node.left is None:
            return node.getValue()
        return self.getMin(node.left)

    def getMax(self, node=None):
        if node is None:
            node = self.node
        if node.right is None:
            return node.getValue()
        return self.getMax(node.right)

    def inOrderPrint(self):
        self._inOrderRecursion(self.node)

    def _inOrderRecursion(self, node):
        if (node is None):
            return
        self._inOrderRecursion(node.left)
        print(node.getValue(), ",", end="")
        self._inOrderRecursion(node.right)

    def preOrderPrint(self):
        self._preOrderRecursion(self.node)

    def _preOrderRecursion(self, node):
        if (node is None):
            return
        print(node.getValue(), ",", end="")
        self._preOrderRecursion(node.left)
        self._preOrderRecursion(node.right)

    def postOrderPrint(self):
        self._postOrderRecursion(self.node)

    def _postOrderRecursion(self, node):
        if (node is None):
            return
        self._postOrderRecursion(node.left)
        self._postOrderRecursion(node.right)
        print(node.getValue(), ",", end="")


def levelOrderPrint(tree):
    queue = []
    node = tree.getNode()
    while node is not None:
        print(node.getValue(), end=",")
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)
        if len(queue) > 0:
            node = queue.pop(0)
        else:
            return


def findLevels(node):
    if (node is None): return 0
    leftHeight = findLevels(node.left)
    rightHeight = findLevels(node.right)
    if leftHeight > rightHeight:
        return leftHeight + 1
    else:
        return rightHeight + 1


tree = BinaryTree()
tree.insertNode(3)
tree.insertNode(0)
tree.insertNode(4)
tree.insertNode(-2)
tree.insertNode(1)
tree.insertNode(8)
print(tree.getMin())
print(tree.getMax())

print("In-Order")
tree.inOrderPrint()
print("")
print("Pre-Order")
tree.preOrderPrint()
print("")
print("Post-Order")
tree.postOrderPrint()
print("")
print("Level-Order")
levelOrderPrint(tree)
print("")
print("Levels")
print(findLevels(tree.getNode()))
