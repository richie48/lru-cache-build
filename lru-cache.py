class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next,self.prev=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        
        #also initializing the dummy left and right pointers so i can easily insert and 
        # delete nodes at the start and end of double linked list
        self.right=Node(0,0)
        self.left=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left
    
    def insert(self,node):
        node.next=self.right
        node.prev=self.right.prev
        self.right.prev.next=node
        self.right.prev=node
        
        
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)