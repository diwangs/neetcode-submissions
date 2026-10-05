class ListNode:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.post = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.post = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # Remove
            node.post.prev = node.prev
            node.prev.post = node.post

            # Insert
            node.post = self.tail
            node.prev = self.tail.prev
            self.tail.prev.post = node
            self.tail.prev = node

            return self.cache[key].v
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].post.prev = self.cache[key].prev
            self.cache[key].prev.post = self.cache[key].post
        
        new = ListNode(key, value)

        # Insert
        new.post = self.tail
        new.prev = self.tail.prev
        self.tail.prev.post = new
        self.tail.prev = new

        self.cache[key] = new

        if len(self.cache) > self.cap:
            self.cache.pop(self.head.post.k)
            
            self.head.post = self.head.post.post
            self.head.post.prev = self.head



        

        
