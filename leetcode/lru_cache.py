# Medium

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.least_recent_key = []

    def get(self, key: int) -> int:
        # print("GET", key)
        # print(self.cache)
        # print(self.least_recent_key)
        ret = self.cache.get(key)
        if ret is not None:
            self.least_recent_key.remove(key)
            self.least_recent_key.append(key)
            return ret
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key] = value
        # Evict
        elif len(self.cache) == self.capacity:
            k = self.least_recent_key.pop(0)
            del self.cache[k]
            self.cache[key] = value
        else:
            self.cache[key] = value
    
        if key in self.least_recent_key:
            self.least_recent_key.remove(key)
        self.least_recent_key.append(key)
        # print("PUT", key, value)
        # print(self.cache)
        # print(self.least_recent_key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Doubly linked-list

class Node:
    def __init__(self, key, val):
        self.prev = None # will be set later
        self.next = None # will be set later
        self.val = val
        self.key = key
    def __str__(self):
        return f'Node(key={self.key}, val={self.val})'
    def __repr__(self) -> str:
        return self.__str__()

class LRUCacheDLL:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map from key to node
        self.tail = None
        self.head = None
    

    def print_dll(self):
        # print("HEAD", self.head, "TAIL", self.tail)
        n = self.head
        cycle = set()

        s = "\t\t"
        s += str(n) + " -> "
        while n != self.tail:
            t = (n.key if n.key else "None", n.val if n.val else "None")
            if t in cycle:
                raise Exception(f"Cycle detected: HEAD {self.head} TAIL {self.tail} STRING {s} {n}")
            cycle.add(t)

            n = n.next
            s += ' ' + str(n) + ' -> '

        print(s)

    def add_node(self, node):
        if self.tail is None: # initialize the DLL
            self.tail = node
            self.head = node
            node.next = None
            node.prev = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = None
        # print("ADDED NODE", node)
        # self._check_invariant()
    
    def _check_invariant(self):
        n = self.head
        while n != self.tail:
            if n.next.prev:
                assert n == n.next.prev, f'error: node {n} has .next {n.next}, but {n.next} has prev {n.next.prev}'
            n = n.next

    def delete_node(self, node) -> int:
        # print("DELETE node", node)
        if node.next:
            if node.prev is not None:
                # print("BEFORE DELETING")
                # self.print_dll()
                # print('PREV', node.prev, 'NEXT', node.next)
                node.prev.next = node.next
                node.next.prev = node.prev
                if self.tail == node:
                    self.tail = node.prev if node.prev else None
                # print("AFTER DELETING")
                # self.print_dll()
            else:
                node.next.prev = None
                self.head = node.next
            if self.head == node:
                self.head = node.next
        else:
            if node.prev is not None:
                node.prev.next = None
                self.tail = node.prev if node.prev else None
            else:
                self.head = None
                self.tail = None
        # self._check_invariant()
        return node.key       

    def get(self, key: int) -> int:
        # print("GET", key)
        # print(self.cache)
        ret = self.cache.get(key)
        # print("KEY", key, "GOT", ret)
        if ret is not None:
            # print("DELETE NODE", ret)
            self.delete_node(ret)
            # self.print_dll()
            self.add_node(ret)
            # print("ADD NODE", ret)
            # self.print_dll()

            # self.print_dll()
            return ret.val
        else:
            # self.print_dll()
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            old_node = self.cache[key]
            self.delete_node(old_node)
            # print("DELETED NODE", old_node)
            # self.print_dll()
            new_node = Node(key, value)
            self.add_node(new_node)
            # print("ADDED NODE", new_node)
            # self.print_dll()
            self.cache[key] = new_node
        # Evict
        elif len(self.cache) == self.capacity:
            # print("EVICT", self.head)
            k = self.delete_node(self.head)
            del self.cache[k]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)
        else:
            new_node = Node(key, value)
            self.add_node(new_node)
            self.cache[key] = new_node
        # print(self.cache)
        # self.print_dll()

class SolutionNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCacheSolution:
    """About 2-3 times faster than my DLL implementation. This is a circular doubly-linked list with sentinels."""
    def __init__(self, capacity):
        self.size = capacity
        self.m = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, p):
        p.prev.next = p.next
        p.next.prev = p.prev

    def addNode(self, newnode):
        temp = self.head.next
        self.head.next = newnode
        newnode.prev = self.head
        newnode.next = temp
        temp.prev = newnode

    def get(self, key):
        if key not in self.m:
            return -1

        p = self.m[key]
        self.deleteNode(p)
        self.addNode(p)
        self.m[key] = self.head.next
        return self.head.next.val

    def put(self, key, value):
        if key in self.m:
            c = self.m[key]
            self.deleteNode(c)
            c.val = value
            self.addNode(c)
            self.m[key] = self.head.next
        else:
            if len(self.m) == self.size:
                prev = self.tail.prev
                self.deleteNode(prev)
                l = Node(key, value)
                self.addNode(l)
                del self.m[prev.key]
                self.m[key] = self.head.next
            else:
                l = Node(key, value)
                self.addNode(l)
                self.m[key] = self.head.next

# Your LRUCache object will be instantiated and called as such:
# inputs = [[10], [10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
inputs = [[1],[2,1],[2]]

obj = LRUCacheDLL(*inputs[0])
for l in inputs[1:]:
    if len(l) == 1:
        
        print("GETTING", l[0])
        print("RECEIVED", obj.get(l[0]))
    else:
        print("PUTTING", l[0], l[1])
        obj.put(l[0], l[1])


# param_1 = obj.get(key)
# obj.put(key,value)