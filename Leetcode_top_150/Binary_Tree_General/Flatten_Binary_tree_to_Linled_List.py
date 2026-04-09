# ======================================================
# FLATTEN BINARY TREE TO LINKED LIST (LeetCode 114)
# ======================================================

# Problem:
# Given the root of a binary tree, flatten the tree into
# a "linked list":
# - The linked list should use the same TreeNode class
# - The right child pointer points to the next node
# - The left child pointer should always be NULL
# - The order should follow preorder traversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Store Preorder then Rebuild)
# ------------------------------------------------------

class BruteForceSolution:
    def flatten(self, root):
        if not root:
            return

        preorder = []

        def dfs(node):
            if not node:
                return
            preorder.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        for i in range(len(preorder) - 1):
            preorder[i].left = None
            preorder[i].right = preorder[i + 1]


# ------------------------------------------------------
# 2️⃣ Recursive (Postorder Modification)
# ------------------------------------------------------

class RecursiveSolution:
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = right


# ------------------------------------------------------
# 3️⃣ Iterative Using Stack (Preorder Simulation)
# ------------------------------------------------------

class StackSolution:
    def flatten(self, root):
        if not root:
            return

        stack = [root]

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if stack:
                node.right = stack[-1]

            node.left = None


# ------------------------------------------------------
# 4️⃣ Reverse Preorder (DFS Right → Left)
# ------------------------------------------------------

class ReversePreorderSolution:
    def flatten(self, root):
        self.prev = None

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Morris Traversal O(1) Space)
# ------------------------------------------------------

class OptimalSolution:
    def flatten(self, root):
        curr = root

        while curr:
            if curr.left:
                # Find rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right

                # Rewire connections
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right
