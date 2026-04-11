# ======================================================
# BINARY SEARCH TREE ITERATOR (LeetCode 173)
# ======================================================

# Problem:
# Implement the BSTIterator class that represents an iterator
# over the in-order traversal of a binary search tree (BST).
#
# Functions:
# - next()    : returns the next smallest number
# - hasNext() : returns True if there exists a next number


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Store Inorder Traversal)
# ------------------------------------------------------

class BSTIteratorBrute:
    def __init__(self, root):
        self.arr = []
        self.index = -1

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self):
        self.index += 1
        return self.arr[self.index]

    def hasNext(self):
        return self.index + 1 < len(self.arr)


# ------------------------------------------------------
# 2️⃣ Better (Generator Approach)
# ------------------------------------------------------

class BSTIteratorGenerator:
    def __init__(self, root):
        self.gen = self.inorder(root)
        self.next_val = None
        self._advance()

    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.val
            yield from self.inorder(node.right)

    def _advance(self):
        try:
            self.next_val = next(self.gen)
        except StopIteration:
            self.next_val = None

    def next(self):
        val = self.next_val
        self._advance()
        return val

    def hasNext(self):
        return self.next_val is not None


# ------------------------------------------------------
# 3️⃣ Stack-Based Inorder Traversal
# ------------------------------------------------------

class BSTIteratorStack:
    def __init__(self, root):
        self.stack = []
        self._pushLeft(root)

    def _pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        self._pushLeft(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0


# ------------------------------------------------------
# 4️⃣ Controlled Recursion (Simulated)
# ------------------------------------------------------

class BSTIteratorControlled:
    def __init__(self, root):
        self.stack = []
        self.curr = root

    def next(self):
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        node = self.stack.pop()
        val = node.val
        self.curr = node.right

        return val

    def hasNext(self):
        return self.curr is not None or len(self.stack) > 0


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Most Asked - O(h) Space)
# ------------------------------------------------------

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._pushLeft(root)

    def _pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        if node.right:
            self._pushLeft(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0




