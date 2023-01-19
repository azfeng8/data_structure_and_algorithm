#!/usr/bin/env python3.8
"""Binary Tree Implementation"""

class Binary_Node:
    """"""
    def __init__(self,x):
        self.item = x
        #TODO: change the below line
        self.left = None
        self.right = None
        self.parent = None
        # self.subtree_update()
    def subtree_iter(self):
        if self.left: yield from self.left.subtree_iter()
        yield self
        if self.right: yield from self.right.subtree_iter()

    # def subtree_iter(self):
    #     if self.right: yield from self.right.subtree_iter()
    #     yield self
    #     if self.left: yield from self.left.subtree_iter()

    def subtree_first(self):
        if self.left: return self.left.subtree_first()
        else: return self
    def subtree_last(self):
        if self.right: return self.right.subtree_last()
        else: return self
    def successor(self):
        if self.right: return self.right.subtree_first()
        while self.parent and (self is self.parent.right):
            self = self.parent
        return self.parent

    def predecessor(self):
        # O(h)
        if self.left: return self.left.subtree_last()
        while self.parent and (self is self.parent.left):
            self = self.parent
        return self.parent

    def subtree_insert_before(self, B):
        if self.left:
            self = self.left.subtree_last()
            self.right, B.parent = B, self
        else:
            self.left, B.parent = B, self
        # A.maintain()
    def subtree_insert_after(self, B):
        if self.right:
            self = A.right.subtree_first()
            self.left, B.parent = B, self
        else:
            self.right, B.parent = B, self 
        # self.maintain()
        # O(h)
        # wait for R07!

    def subtree_delete(self):
        # O(h)
        if self.left or self.right:
        # self is not a leaf
            if self.left: B = self.predecessor()
            else:
                B = self.successor()
                self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
        # self is a leaf
            if self.parent.left is self: self.parent.left = None
            else:
                self.parent.right = None
            # self.parent.maintain()
            # wait for R07!
            return self

class Binary_Tree:
    def __init__(self, Node_Type = Binary_Node):
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type

    def __len__(self): return self.size
    def __iter__(self):
        if self.root:
            for A in self.root.subtree_iter():
                yield A.item

class BST_Node(Binary_Node):
    """_summary_

    Args:
        Binary_Node (_type_): _description_
    """
    def subtree_find(A, k):
    # O(h)
        if k < A.item:
            if A.left: return A.left.subtree_find(k)
        elif k > A.item:
            if A.right: return A.right.subtree_find(k)
        else:
            return A
        return None

    def subtree_find_next(A, k):
        # O(h)
        if A.item <= k:
            if A.right: return A.right.subtree_find_next(k)
            else:
                return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B:
                return B
        return A

    def subtree_find_prev(A, k):
    # O(h)
        if A.item >= k:
            if A.left: return A.left.subtree_find_prev(k)
            else: return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B: return B
        return A

    def subtree_insert(A, B):
    # O(h)
        if B.item < A.item:
            if A.left: A.left.subtree_insert(B)
            else: A.subtree_insert_before(B)
        elif B.item > A.item:
            if A.right: A.right.subtree_insert(B)
            else:
                A.subtree_insert_after(B)
        else:
            A.item = B.item


class Set_Binary_Tree(Binary_Tree): # Binary Search Tree
    def __init__(self): super().__init__(BST_Node)
    def iter_order(self): yield from self
    def build(self, X):
        for x in X: self.insert(x)
    def find_min(self):
        if self.root:
            return self.root.subtree_first().item

    def find(self, k):
        if self.root: node = self.root.subtree_find(k)
        if node: return node.item
    
    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
        if node:
            return node.item
    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
        if node:
            return node.item
    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:
            self.root = new_node
        self.size += 1
        return True
    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item