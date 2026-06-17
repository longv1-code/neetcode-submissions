class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val # each Node stores a key and val
        self.prev = self.next = None # their prev and next pointers are set to None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity # Object stores capacity to reference at another function
        self.cache = {} # hashmap cache {key : Node(key, value)}
 
        self.left, self.right = Node(0, 0), Node(0, 0) # dummy nodes for LRU and MRU
        self.left.next, self.right.prev = self.right, self.left # dummy nodes pointing to each other

    def remove(self, node): # removes Node from the list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node): # inserts Node to the right -> MRU
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache: # checks if key is in cache
            self.remove(self.cache[key]) # removes Node
            self.insert(self.cache[key]) # moves Node to MRU
            return self.cache[key].val # returns the value of Node
        return -1 # if it doesn't exist, return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # checks if key is in cache
            self.remove(self.cache[key]) # removes Node
        self.cache[key] = Node(key, value) # creates / updates key in cache with new Node
        self.insert(self.cache[key]) # inserts new Node to the right

        if len(self.cache) > self.cap: # compares length of cache to capacity 
            lru = self.left.next # LRU node from our LRU dummy node next 
            self.remove(lru) # removes LRU node from linked list
            del self.cache[lru.key] # removes LRU node from cache