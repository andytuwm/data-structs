__author__ = 'Andy'


class LinkedHashEntry:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, nextVal):
        self.next = nextVal

    def setVal(self, value):
        self.value = value

    def getVal(self):
        return self.value


class HashTableSet:
    # default capacity 1000 elements
    def __init__(self, capacity=1009):
        self.capacity = capacity
        self._size = 0
        # self.keys = [] add keys list to write a hashmap
        self.values = [LinkedHashEntry(None)] * self.capacity

    # Separate chaining collision resolution
    # checks if a value already exists in set within the chain.
    def checkLinkedExistence(self, linkedEntry, value):
        if linkedEntry.getVal() == value:
            return True
        if linkedEntry.getNext() is not None:
            return self.checkLinkedExistence(linkedEntry.getNext(), value)
        return False

    # finds the next available linked entry in the chain at a particular hash slot
    def findAvailableLinkedEntry(self, linkedEntry):
        if linkedEntry.getNext() is None:
            linkedEntry.setNext(LinkedHashEntry())
            return linkedEntry.getNext()
        else:
            return self.findAvailableLinkedEntry(linkedEntry.getNext())

    # searches the chain for a specific value and returns the found node along with it's parent
    # in (parent, foundnode) format
    def findLinkedEntryVal(self, linkedEntry, value, prev=None):
        if linkedEntry.getVal() == value:
            return prev, linkedEntry
        if linkedEntry.getNext() is not None:
            prev = linkedEntry
            return self.findLinkedEntryVal(linkedEntry.getNext(), value, prev)
        else:
            return False

    def hashingfn(self, value):
        return hash(value) % self.capacity

    def put(self, value):
        hashkey = self.hashingfn(value)
        if not self.checkLinkedExistence(self.values[hashkey], value):
            self.findAvailableLinkedEntry(self.values[hashkey]).setVal(value)
            self._size += 1

    def contains(self, value):
        hashkey = self.hashingfn(value)
        if self.checkLinkedExistence(self.values[hashkey], value):
            return True
        return False

    def delete(self, value):
        hashkey = self.hashingfn(value)
        if self.checkLinkedExistence(self.values[hashkey], value):
            parent, entry = self.findLinkedEntryVal(self.values[hashkey], value)
            if entry is not False:
                parent.setNext(entry.getNext())
                self._size -= 1

    def size(self):
        return self._size