__author__ = 'Andy'


class Node:
    def __init__(self, value=None):
        self.path = []
        self.value = value
        self.valueExists = False


class Trie:
    def __init__(self):
        self.node = Node()

    def insertWord(self, word):
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
        if node is None:
            node = self.node
        if i == len(word) and node.valueExists is True: return True
        index = self.findNode(node, word[i])
        if index > -1:
            return self.contains(word, node.path[index], i + 1)
        else:
            return False


trie = Trie()
trie.insertWord("hello")
trie.insertWord("hella")
trie.insertWord("apple")
print(trie.contains("hello"))
print(trie.contains("hella"))
print(trie.contains("apple"))
print(trie.contains("hello!"))