# ======================================================
# REMOVE Nth NODE FROM END OF LIST - ALL APPROACHES
# ======================================================

# Problem (LeetCode 19):
# Given the head of a linked list, remove the nth node from the end
# and return its head.
#
# Example:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Two Pass - Length Count)
# ------------------------------------------------------

class BruteForceSolution:
    def removeNthFromEnd(self, head, n):

        # Step 1: find length
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        # Step 2: find node before target
        target = length - n

        dummy = ListNode(0, head)
        curr = dummy

        for _ in range(target):
            curr = curr.next

        # remove node
        curr.next = curr.next.next

        return dummy.next


# ------------------------------------------------------
# 2️⃣ Two Pointer (Single Pass) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0, head)
        fast = slow = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both until fast reaches end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # remove node
        slow.next = slow.next.next

        return dummy.next


# ------------------------------------------------------
# 3️⃣ Stack Based Approach
# ------------------------------------------------------

class StackSolution:
    def removeNthFromEnd(self, head, n):

        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        dummy = ListNode(0, head)

        # pop n nodes
        for _ in range(n):
            node = stack.pop()

        prev = stack[-1] if stack else dummy
        prev.next = node.next

        return dummy.next


# ------------------------------------------------------
# 4️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def removeNthFromEnd(self, head, n):

        def dfs(node):
            if not node:
                return 0

            idx = dfs(node.next) + 1

            if idx == n + 1:
                node.next = node.next.next

            return idx

        dummy = ListNode(0, head)
        dfs(dummy)
        return dummy.next


# ------------------------------------------------------
# 5️⃣ Using List Conversion
# ------------------------------------------------------

class ListSolution:
    def removeNthFromEnd(self, head, n):

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        idx = len(nodes) - n

        if idx == 0:
            return head.next

        nodes[idx - 1].next = nodes[idx].next

        return head


