# ======================================================
# KTH SMALLEST ELEMENT IN BST (LeetCode 230)
# ======================================================

# Problem:
# Given the root of a Binary Search Tree (BST) and an integer k,
# return the kth smallest value (1-indexed) of all the values
# of the nodes in the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Store + Sort)
# ------------------------------------------------------

class BruteForceSolution:
    def kthSmallest(self, root, k):
        values = []

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        values.sort()

        return values[k - 1]


# ------------------------------------------------------
# 2️⃣ Better (Inorder Traversal → Array)
# ------------------------------------------------------

class BetterSolution:
    def kthSmallest(self, root, k):
        inorder = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        return inorder[k - 1]


# ------------------------------------------------------
# 3️⃣ DFS with Counter (Early Stop)
# ------------------------------------------------------

class DFSSolution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return

            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.result


# ------------------------------------------------------
# 4️⃣ Iterative Inorder (Stack)
# ------------------------------------------------------

class IterativeSolution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Inorder Traversal)
# ------------------------------------------------------

class OptimalSolution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right





