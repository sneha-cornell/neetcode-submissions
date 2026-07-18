#hash (O(1) key lookup) & doubly linked list (O(1) removal, insertion at any position)
#ordereddict version if built ins are allowed 

class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache={}
        self.head = Node() #most recently used side 
        self.tail = Node() #least recently used side 
        self.head.next = self.tail 
        self.tail.prev = self.head

    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    #self.head->node->self.head.next
    def _add_front(self,node):
        node.prev = self.head
        node.next = self.head.next 
        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        node = self.cache[key]
        #when we get/access, it counts as a use so we move it to MRU
        self._remove(node)
        self._add_front(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self._remove(self.cache[key])
        node = Node(key,value)
        self.cache[key]=node
        self._add_front(node)
        if len(self.cache)>self.capacity: 
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
