# ======================================================
# COUNT COMPLETE TREE NODES (LeetCode 222)
# ======================================================

# Problem:
# Given the root of a complete binary tree, return the
# number of the nodes in the tree.
#
# A complete binary tree is a binary tree in which every
# level, except possibly the last, is completely filled,
# and all nodes are as far left as possible.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Traverse All Nodes)
# ------------------------------------------------------

class BruteForceSolution:
    def countNodes(self, root):
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# ------------------------------------------------------
# 2️⃣ BFS (Level Order Traversal)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def countNodes(self, root):
        if not root:
            return 0

        queue = deque([root])
        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return count


# ------------------------------------------------------
# 3️⃣ DFS (Iterative using Stack)
# ------------------------------------------------------

class DFSSolution:
    def countNodes(self, root):
        if not root:
            return 0

        stack = [root]
        count = 0

        while stack:
            node = stack.pop()
            count += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return count


# ------------------------------------------------------
# 4️⃣ Height-Based Optimization
# ------------------------------------------------------

class HeightSolution:
    def countNodes(self, root):
        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def getRightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        if not root:
            return 0

        left_h = getLeftHeight(root)
        right_h = getRightHeight(root)

        # Perfect binary tree
        if left_h == right_h:
            return (1 << left_h) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Log^2 N)
# ------------------------------------------------------

class OptimalSolution:
    def countNodes(self, root):
        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def rightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        if not root:
            return 0

        lh = leftHeight(root)
        rh = rightHeight(root)

        # If heights match → perfect tree
        if lh == rh:
            return (1 << lh) - 1

        # Otherwise recurse
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
