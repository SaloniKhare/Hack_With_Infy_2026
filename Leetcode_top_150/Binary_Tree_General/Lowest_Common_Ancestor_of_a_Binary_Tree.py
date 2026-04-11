# ======================================================
# LOWEST COMMON ANCESTOR OF A BINARY TREE (LeetCode 236)
# ======================================================

# Problem:
# Given a binary tree, find the lowest common ancestor (LCA)
# of two given nodes p and q.
#
# The LCA is defined as the lowest node in the tree that has
# both p and q as descendants (a node can be a descendant of itself).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# ------------------------------------------------------
# 1️⃣ Brute Force (Store Paths)
# ------------------------------------------------------

class BruteForceSolution:
    def lowestCommonAncestor(self, root, p, q):
        def getPath(node, target, path):
            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            if (getPath(node.left, target, path) or
                getPath(node.right, target, path)):
                return True

            path.pop()
            return False

        path1, path2 = [], []
        getPath(root, p, path1)
        getPath(root, q, path2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1

        return path1[i - 1]


# ------------------------------------------------------
# 2️⃣ Recursive DFS (Standard)
# ------------------------------------------------------

class RecursiveSolution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


# ------------------------------------------------------
# 3️⃣ Iterative (Parent Pointer Map)
# ------------------------------------------------------

class IterativeSolution:
    def lowestCommonAncestor(self, root, p, q):
        parent = {root: None}
        stack = [root]

        # Build parent map
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()

        # Store ancestors of p
        while p:
            ancestors.add(p)
            p = parent[p]

        # Find first common ancestor
        while q not in ancestors:
            q = parent[q]

        return q


# ------------------------------------------------------
# 4️⃣ Path Comparison (Simplified)
# ------------------------------------------------------

class PathComparisonSolution:
    def lowestCommonAncestor(self, root, p, q):
        def getPath(node, target):
            if not node:
                return None

            if node == target:
                return [node]

            left = getPath(node.left, target)
            if left:
                return [node] + left

            right = getPath(node.right, target)
            if right:
                return [node] + right

            return None

        path1 = getPath(root, p)
        path2 = getPath(root, q)

        lca = None
        for u, v in zip(path1, path2):
            if u == v:
                lca = u
            else:
                break

        return lca


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Most Asked)
# ------------------------------------------------------

class OptimalSolution:
    def lowestCommonAncestor(self, root, p, q):
        # Base case
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return non-null → current node is LCA
        if left and right:
            return root

        # Otherwise return the non-null side
        return left if left else right
