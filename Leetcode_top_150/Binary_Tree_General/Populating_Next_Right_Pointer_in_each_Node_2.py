# ======================================================
# POPULATING NEXT RIGHT POINTER IN EACH NODE II
# (LeetCode 117)
# ======================================================

# Problem:
# Given a binary tree (not necessarily perfect),
# populate each next pointer to point to its next right node.
# If there is no next right node, set it to NULL.
# You must use constant extra space.


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Level Order Traversal using Queue)
# ------------------------------------------------------

from collections import deque

class BruteForceSolution:
    def connect(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


# ------------------------------------------------------
# 2️⃣ Better Approach (Level Order without size var)
# ------------------------------------------------------

class BetterSolution:
    def connect(self, root):
        if not root:
            return None

        queue = deque([root, None])  # None marks level end

        while queue:
            node = queue.popleft()

            if node:
                node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if queue:
                    queue.append(None)

        return root


# ------------------------------------------------------
# 3️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def connect(self, root):
        if not root:
            return None

        def dfs(node):
            if not node:
                return

            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = self.getNext(node.next)

            if node.right:
                node.right.next = self.getNext(node.next)

            # Important: process right before left
            dfs(node.right)
            dfs(node.left)

        def getNext(node):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next
            return None

        self.getNext = getNext
        dfs(root)
        return root


# ------------------------------------------------------
# 4️⃣ Iterative Using Dummy Node (Level by Level)
# ------------------------------------------------------

class DummyNodeSolution:
    def connect(self, root):
        if not root:
            return None

        curr = root

        while curr:
            dummy = Node(0)
            tail = dummy

            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            curr = dummy.next

        return root


# ------------------------------------------------------
# 5️⃣ Optimal Solution ⭐ (Constant Space, Most Asked)
# ------------------------------------------------------

class OptimalSolution:
    def connect(self, root):
        if not root:
            return None

        curr = root

        while curr:
            dummy = Node(0)
            tail = dummy

            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                curr = curr.next

            curr = dummy.next  # move to next level

        return root
