class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.currentCount = 0
        self.keyMap = {}

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        value = self.keyMap[key].value
        self.remove(key)
        self.add(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            self.remove(key)
        if self.capacity == len(self.keyMap):
            self.remove(self.head.key)
        self.add(key, value)
        
    def remove(self, key):
        currNode = self.keyMap.get(key)
        if currNode.prev == None:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        
        elif currNode.next == None:
            currNode.prev.next = None
            self.tail = currNode.prev

# 
        
        else:
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev

        del self.keyMap[key]
        del currNode

        self.currentCount -= 1


        # removing head 
        # removing tail
        # removing middle value

    def add(self, key, value):
        newNode = Node(key, value)

        if self.currentCount == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode


        self.keyMap[key] = newNode
        self.currentCount += 1

        # 1 -> tail is None or currentCount is 0
        # 2 -> tail is not None or currentCount > 0



class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
