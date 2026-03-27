# ======================================================
# COPY LIST WITH RANDOM POINTER - ALL APPROACHES
# ======================================================

# Problem (LeetCode 138):
# A linked list where each node has:
# - next pointer
# - random pointer (can point to any node or None)
#
# Return a deep copy of the list.
#
# Example:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: Deep copied list


# ------------------------------------------------------
# Definition for Node
# ------------------------------------------------------

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Array)
# ------------------------------------------------------

class BruteForceSolution:
    def copyRandomList(self, head):

        if not head:
            return None

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        # create new nodes
        new_nodes = [Node(node.val) for node in nodes]

        # mapping index
        index_map = {node: i for i, node in enumerate(nodes)}

        for i, node in enumerate(nodes):

            if i < len(nodes) - 1:
                new_nodes[i].next = new_nodes[i + 1]

            if node.random:
                new_nodes[i].random = new_nodes[index_map[node.random]]

        return new_nodes[0]


# ------------------------------------------------------
# 2️⃣ HashMap (Most Important)
# ------------------------------------------------------

class HashMapSolution:
    def copyRandomList(self, head):

        if not head:
            return None

        old_to_new = {}

        curr = head

        # Step 1: create nodes
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: assign next & random
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]


# ------------------------------------------------------
# 3️⃣ Optimized (O(1) Space Trick) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def copyRandomList(self, head):

        if not head:
            return None

        # Step 1: Insert copied nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate lists
        curr = head
        new_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return new_head


# ------------------------------------------------------
# 4️⃣ Recursive + HashMap
# ------------------------------------------------------

class RecursiveSolution:
    def copyRandomList(self, head):

        visited = {}

        def dfs(node):
            if not node:
                return None

            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node] = copy

            copy.next = dfs(node.next)
            copy.random = dfs(node.random)

            return copy

        return dfs(head)


# ------------------------------------------------------
# 5️⃣ Using DefaultDict
# ------------------------------------------------------

from collections import defaultdict

class DefaultDictSolution:
    def copyRandomList(self, head):

        old_to_new = defaultdict(lambda: Node(0))

        old_to_new[None] = None

        curr = head

        while curr:
            old_to_new[curr].val = curr.val
            old_to_new[curr].next = old_to_new[curr.next]
            old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]


# ------------------------------------------------------
# Example (Simple)
# ------------------------------------------------------

# Creating small list:
# 1 -> 2
# random pointers:
# 1.random = 2
# 2.random = 1

n1 = Node(1)
n2 = Node(2)

n1.next = n2
n1.random = n2
n2.random = n1

copied = OptimalSolution().copyRandomList(n1)

print("Original:", n1.val, "->", n1.next.val)
print("Copied:", copied.val, "->", copied.next.val)
