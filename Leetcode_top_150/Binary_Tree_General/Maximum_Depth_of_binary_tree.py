# ======================================================
# MAXIMUM DEPTH OF BINARY TREE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 104):
# Given the root of a binary tree, return its maximum depth.
#
# Maximum depth = number of nodes along the longest path
# from root down to the farthest leaf node.
#
# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3


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
    def maxDepth(self, root):

        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


# ------------------------------------------------------
# 2️⃣ Iterative DFS (Stack)
# ------------------------------------------------------

class DFSStackSolution:
    def maxDepth(self, root):

        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:

            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth


# ------------------------------------------------------
# 3️⃣ BFS (Level Order Traversal)
# ------------------------------------------------------

from collections import deque

class BFSSolution:
    def maxDepth(self, root):

        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth


# ------------------------------------------------------
# 4️⃣ One-Liner Recursive
# ------------------------------------------------------

class OneLinerSolution:
    def maxDepth(self, root):
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ------------------------------------------------------
# 5️⃣ BFS with Depth Tracking
# ------------------------------------------------------

class BFSDepthSolution:
    def maxDepth(self, root):

        if not root:
            return 0

        queue = [(root, 1)]
        max_depth = 0

        while queue:

            node, depth = queue.pop(0)

            if node:
                max_depth = max(max_depth, depth)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return max_depth


# ------------------------------------------------------
# Example
# ------------------------------------------------------

#       3
#      / \
#     9  20
#        / \
#       15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print("Recursive:", RecursiveSolution().maxDepth(root))
print("DFS Stack:", DFSStackSolution().maxDepth(root))
print("BFS:", BFSSolution().maxDepth(root))
print("One-liner:", OneLinerSolution().maxDepth(root))
print("BFS Depth:", BFSDepthSolution().maxDepth(root))
