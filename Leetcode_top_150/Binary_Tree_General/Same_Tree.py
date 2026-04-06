# ======================================================
# SAME TREE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 100):
# Given two binary trees p and q,
# check if they are the same or not.
#
# Two trees are the same if:
# - They are structurally identical
# - Nodes have same values
#
# Example:
# Input: p = [1,2,3], q = [1,2,3]
# Output: True


# ------------------------------------------------------
# Definition for a binary tree node
# ------------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Recursive DFS (Most Important)
# ------------------------------------------------------

class RecursiveSolution:
    def isSameTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# ------------------------------------------------------
# 2️⃣ Iterative BFS (Queue)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def isSameTree(self, p, q):

        queue = deque([(p, q)])

        while queue:

            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True


# ------------------------------------------------------
# 3️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class DFSStackSolution:
    def isSameTree(self, p, q):

        stack = [(p, q)]

        while stack:

            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True


# ------------------------------------------------------
# 4️⃣ Convert to List (Traversal Compare)
# ------------------------------------------------------

class ListSolution:
    def isSameTree(self, p, q):

        def dfs(node):
            if not node:
                return [None]
            return [node.val] + dfs(node.left) + dfs(node.right)

        return dfs(p) == dfs(q)


# ------------------------------------------------------
# 5️⃣ Pythonic One-Liner
# ------------------------------------------------------

class PythonicSolution:
    def isSameTree(self, p, q):
        return (
            p is q or
            (p and q and p.val == q.val and
             self.isSameTree(p.left, q.left) and
             self.isSameTree(p.right, q.right))
        )


# ------------------------------------------------------
# Example
# ------------------------------------------------------

# Tree 1
p = TreeNode(1, TreeNode(2), TreeNode(3))

# Tree 2
q = TreeNode(1, TreeNode(2), TreeNode(3))

print("Recursive:", RecursiveSolution().isSameTree(p, q))
print("BFS:", BFSSolution().isSameTree(p, q))
print("DFS Stack:", DFSStackSolution().isSameTree(p, q))
print("List:", ListSolution().isSameTree(p, q))
print("Pythonic:", PythonicSolution().isSameTree(p, q))
