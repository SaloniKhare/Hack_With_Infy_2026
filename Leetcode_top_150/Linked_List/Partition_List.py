# ======================================================
# PARTITION LIST - ALL APPROACHES
# ======================================================

# Problem (LeetCode 86):
# Given a linked list and a value x,
# partition it such that all nodes < x come before nodes >= x.
#
# Important:
# Maintain relative order of nodes in each partition.
#
# Example:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Array)
# ------------------------------------------------------

class BruteForceSolution:
    def partition(self, head, x):

        less = []
        greater = []

        curr = head

        while curr:
            if curr.val < x:
                less.append(curr.val)
            else:
                greater.append(curr.val)
            curr = curr.next

        arr = less + greater

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 2️⃣ Two List Approach ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def partition(self, head, x):

        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        curr = head

        while curr:

            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        # connect lists
        greater.next = None
        less.next = greater_dummy.next

        return less_dummy.next


# ------------------------------------------------------
# 3️⃣ In-Place Rearrangement
# ------------------------------------------------------

class InPlaceSolution:
    def partition(self, head, x):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        tail = dummy
        while tail.next:
            tail = tail.next

        end = tail

        while curr != end.next:

            if curr.val >= x:
                next_node = curr.next
                tail.next = curr
                curr.next = None
                prev.next = next_node
                tail = curr
                curr = next_node
            else:
                prev = curr
                curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 4️⃣ Using Deque
# ------------------------------------------------------

from collections import deque

class DequeSolution:
    def partition(self, head, x):

        less = deque()
        greater = deque()

        curr = head

        while curr:
            if curr.val < x:
                less.append(curr.val)
            else:
                greater.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy

        for num in list(less) + list(greater):
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 5️⃣ Stable Partition (Clean Version)
# ------------------------------------------------------

class CleanSolution:
    def partition(self, head, x):

        before = ListNode(0)
        after = ListNode(0)

        b = before
        a = after

        while head:
            if head.val < x:
                b.next = head
                b = b.next
            else:
                a.next = head
                a = a.next
            head = head.next

        a.next = None
        b.next = after.next

        return before.next


# ------------------------------------------------------
# Example
# ------------------------------------------------------

# 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
# Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5

head = ListNode(1,
        ListNode(4,
        ListNode(3,
        ListNode(2,
        ListNode(5,
        ListNode(2))))))

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

res = OptimalSolution().partition(head, 3)
print_list(res)
