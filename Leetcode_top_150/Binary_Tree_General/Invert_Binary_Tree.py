# ======================================================
# INVERT BINARY TREE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 226):
# Given the root of a binary tree, invert the tree.
#
# Inversion means:
# Swap left and right child of every node.
#
# Example:
# Input:
#       4
#     /   \
#    2     7
#   / \   / \
#  1   3 6   9
#
# Output:
#       4
#     /   \
#    7     2
#   / \   / \
#  9   6 3   1


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
    def invertTree(self, root):

        if not root:
            return None

        # swap left and right
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# ------------------------------------------------------
# 2️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class DFSStackSolution:
    def invertTree(self, root):

        if not root:
            return None

        stack = [root]

        while stack:

            node = stack.pop()

            # swap
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root


# ------------------------------------------------------
# 3️⃣ BFS (Level Order)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def invertTree(self, root):

        if not root:
            return None

        queue = deque([root])

        while queue:

            node = queue.popleft()

            # swap
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


# ------------------------------------------------------
# 4️⃣ One-Liner Recursive
# ------------------------------------------------------

class OneLinerSolution:
    def invertTree(self, root):
        return None if not root else TreeNode(
            root.val,
            self.invertTree(root.right),
            self.invertTree(root.left)
        )


# ------------------------------------------------------
# 5️⃣ Using Queue (Simplified)
# ------------------------------------------------------

class QueueSolution:
    def invertTree(self, root):

        if not root:
            return None

        queue = [root]

        for node in queue:
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
