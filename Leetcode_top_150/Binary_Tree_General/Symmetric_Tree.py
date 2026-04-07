# ======================================================
# SYMMETRIC TREE (LeetCode 101)
# ======================================================

# Problem:
# Given the root of a binary tree, check whether it is
# a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Check Mirror by Creating Copy)
# ------------------------------------------------------

class BruteForceSolution:
    def isSymmetric(self, root):
        def invert(node):
            if not node:
                return None
            new_node = TreeNode(node.val)
            new_node.left = invert(node.right)
            new_node.right = invert(node.left)
            return new_node

        def isSame(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isSame(t1.left, t2.left) and
                    isSame(t1.right, t2.right))

        inverted = invert(root)
        return isSame(root, inverted)


# ------------------------------------------------------
# 2️⃣ Recursive Mirror Check (DFS)
# ------------------------------------------------------

class RecursiveSolution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))

        return isMirror(root, root)


# ------------------------------------------------------
# 3️⃣ Iterative BFS (Queue)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def isSymmetric(self, root):
        queue = deque([root, root])

        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False

            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True


# ------------------------------------------------------
# 4️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class DFSSolution:
    def isSymmetric(self, root):
        stack = [(root, root)]

        while stack:
            t1, t2 = stack.pop()

            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False

            stack.append((t1.left, t2.right))
            stack.append((t1.right, t2.left))

        return True


# ------------------------------------------------------
# 5️⃣ Optimal Recursive (Clean & Most Asked) ⭐
# ------------------------------------------------------

class OptimalSolution:
    def isSymmetric(self, root):
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            return check(left.left, right.right) and \
                   check(left.right, right.left)

        return check(root, root)
