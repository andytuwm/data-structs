__author__ = 'Andy'


class Node:
    def __init__(self, value=None):
        self.path = []
        self.value = value
        self.valueExists = False

    def hasChildren(self):
        if len(self.path) > 0: return True
        return False


class Trie:
    def __init__(self):
        self.node = Node()

    def insertWord(self, word):
        word = word.lower()
        index = self.findNode(self.node, word[0])
        if index > -1:
            self.insertChar(self.node.path[index], word[1:])
        else:
            n = Node(word[0])
            self.node.path.append(n)
            self.insertChar(n, word[1:])

    def insertChar(self, node, word):
        if len(word) > 0:
            index = self.findNode(node, word[0])
            if index > -1:
                self.insertChar(node.path[index], word[1:])
            else:
                if len(word) > 1:
                    n = Node(word[0])
                    node.path.append(n)
                    self.insertChar(n, word[1:])
                else:
                    n = Node(word[0])
                    n.valueExists = True
                    node.path.append(n)

    def findNode(self, node, char):
        for i, x in enumerate(node.path):
            if x.value == char:
                return i
        return -1;

    def contains(self, word, node=None, i=0):
        word = word.lower()
        if node is None:
            node = self.node
        if i == len(word) and node.valueExists is True: return True
        index = self.findNode(node, word[i])
        if index > -1:
            return self.contains(word, node.path[index], i + 1)
        else:
            return False


def findDepth(node):
    if node is None: return 0
    maxDepth = 0
    for i, n in enumerate(node.path):
        depth = findDepth(n)
        if depth > maxDepth:
            maxDepth = depth
    return maxDepth + 1


def longestPath(node):
    maxList = [0, 0]
    list = []
    if node.hasChildren:
        for n in node.path:
            d = findDepth(n)
            if d > maxList[0]:
                maxList[0] = d
            elif d > maxList[1]:
                maxList[1] = d
            list.append(longestPath(n))
        list.append(maxList[0] + maxList[1] + 1)
        return max(list)
    return -1


trie = Trie()
trie.insertWord("hello")
trie.insertWord("hella")
trie.insertWord("hellp")
trie.insertWord("holla")
trie.insertWord("holograms")
trie.insertWord("apple")
print(trie.contains("hello"))
print(trie.contains("hella"))
print(trie.contains("apple"))
print(trie.contains("hello!"))
print(findDepth(trie.node))
print(longestPath(trie.node))
