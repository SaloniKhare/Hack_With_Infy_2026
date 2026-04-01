# ======================================================
# LRU CACHE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 146):
# Design a data structure that follows the constraints of
# a Least Recently Used (LRU) cache.
#
# Implement:
# get(key)    -> return value if exists else -1
# put(key,val)-> insert/update key
#
# Capacity fixed. Remove least recently used when full.
#
# All operations must be O(1)


# ------------------------------------------------------
# 1️⃣ Brute Force (List)
# ------------------------------------------------------

class BruteForceLRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def get(self, key):
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                self.cache.append(self.cache.pop(i))
                return v
        return -1

    def put(self, key, value):
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                self.cache.pop(i)
                self.cache.append((key, value))
                return

        if len(self.cache) == self.capacity:
            self.cache.pop(0)

        self.cache.append((key, value))


# ------------------------------------------------------
# 2️⃣ OrderedDict (Python Built-in)
# ------------------------------------------------------

from collections import OrderedDict

class OrderedDictLRU:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# ------------------------------------------------------
# 3️⃣ Optimal (DLL + HashMap) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class OptimalLRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # dummy nodes
        self.left = Node(0, 0)   # LRU
        self.right = Node(0, 0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    # remove node
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert at right (MRU)
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# ------------------------------------------------------
# 4️⃣ Using Deque + Dict (Not Fully O(1))
# ------------------------------------------------------

from collections import deque

class DequeLRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.order.remove(key)

        elif len(self.cache) == self.capacity:
            lru = self.order.popleft()
            del self.cache[lru]

        self.cache[key] = value
        self.order.append(key)


# ------------------------------------------------------
# 5️⃣ Simplified Interview Version
# ------------------------------------------------------

class SimpleLRU:

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.order.remove(key)

        elif len(self.cache) == self.cap:
            lru = self.order.pop(0)
            del self.cache[lru]

        self.cache[key] = value
        self.order.append(key)
