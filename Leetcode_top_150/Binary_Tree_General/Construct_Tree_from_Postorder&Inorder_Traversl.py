# ======================================================
# CONSTRUCT BINARY TREE FROM POSTORDER AND INORDER
# (LeetCode 106)
# ======================================================

# Problem:
# Given two integer arrays inorder and postorder where:
# - inorder is the inorder traversal of a binary tree
# - postorder is the postorder traversal of the same tree
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
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        return root


# ------------------------------------------------------
# 2️⃣ Better Approach (Using HashMap)
# ------------------------------------------------------

class BetterSolution:
    def buildTree(self, inorder, postorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None

            root_val = postorder[post_end]
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            left_size = mid - in_start

            root.left = helper(in_start,
                               mid - 1,
                               post_start,
                               post_start + left_size - 1)

            root.right = helper(mid + 1,
                                in_end,
                                post_start + left_size,
                                post_end - 1)

            return root

        return helper(0, len(inorder)-1, 0, len(postorder)-1)


# ------------------------------------------------------
# 3️⃣ Iterative (Using Stack)
# ------------------------------------------------------

class IterativeSolution:
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_index = len(inorder) - 1

        for i in range(len(postorder) - 2, -1, -1):
            node = TreeNode(postorder[i])

            if stack[-1].val != inorder[inorder_index]:
                stack[-1].right = node
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    last = stack.pop()
                    inorder_index -= 1
                last.left = node

            stack.append(node)

        return root


# ------------------------------------------------------
# 4️⃣ Optimized Recursive (Index Pointer)
# ------------------------------------------------------

class OptimizedSolution:
    def buildTree(self, inorder, postorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)
            mid = inorder_map[root_val]

            # IMPORTANT: build right subtree first
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Most Asked)
# ------------------------------------------------------

class OptimalSolution:
    def buildTree(self, inorder, postorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def build(left, right):
            nonlocal post_idx

            if left > right:
                return None

            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)
            mid = inorder_map[root_val]

            # Build right before left (key insight)
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)



