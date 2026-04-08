# ======================================================
# CONSTRUCT BINARY TREE FROM PREORDER AND INORDER
# (LeetCode 105)
# ======================================================

# Problem:
# Given two integer arrays preorder and inorder where:
# - preorder is the preorder traversal of a binary tree
# - inorder is the inorder traversal of the same tree
# Construct and return the binary tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------
# 1️⃣ Brute Force (Slicing Arrays)
# ------------------------------------------------------

class BruteForceSolution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


# ------------------------------------------------------
# 2️⃣ Better Approach (Avoid Repeated Search using Map)
# ------------------------------------------------------

class BetterSolution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            left_size = mid - in_start

            root.left = helper(pre_start + 1,
                               pre_start + left_size,
                               in_start,
                               mid - 1)

            root.right = helper(pre_start + left_size + 1,
                                pre_end,
                                mid + 1,
                                in_end)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


# ------------------------------------------------------
# 3️⃣ Iterative (Using Stack)
# ------------------------------------------------------

class IterativeSolution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if stack[-1].val != inorder[inorder_index]:
                stack[-1].left = node
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    last = stack.pop()
                    inorder_index += 1
                last.right = node
            stack.append(node)

        return root


# ------------------------------------------------------
# 4️⃣ Optimized Recursive (Index Pointer)
# ------------------------------------------------------

class OptimizedSolution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Most Asked)
# ------------------------------------------------------

class OptimalSolution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx

            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)
            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)


