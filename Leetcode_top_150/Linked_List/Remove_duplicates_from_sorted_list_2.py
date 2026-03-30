# ======================================================
# REMOVE DUPLICATES FROM SORTED LIST - ALL APPROACHES
# ======================================================

# Problem (LeetCode 83):
# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
#
# Example:
# Input: 1 -> 1 -> 2 -> 3 -> 3
# Output: 1 -> 2 -> 3


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Set)
# ------------------------------------------------------

class BruteForceSolution:
    def deleteDuplicates(self, head):

        seen = set()
        dummy = ListNode(0)
        curr_new = dummy
        curr = head

        while curr:

            if curr.val not in seen:
                seen.add(curr.val)
                curr_new.next = ListNode(curr.val)
                curr_new = curr_new.next

            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 2️⃣ Iterative (Most Important)
# ------------------------------------------------------

class OptimalSolution:
    def deleteDuplicates(self, head):

        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


# ------------------------------------------------------
# 3️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def deleteDuplicates(self, head):

        if not head or not head.next:
            return head

        head.next = self.deleteDuplicates(head.next)

        return head if head.val != head.next.val else head.next


# ------------------------------------------------------
# 4️⃣ Using Dummy Node
# ------------------------------------------------------

class DummySolution:
    def deleteDuplicates(self, head):

        dummy = ListNode(0)
        dummy.next = head
        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 5️⃣ Convert to Array
# ------------------------------------------------------

class ArraySolution:
    def deleteDuplicates(self, head):

        arr = []
        curr = head

        while curr:
            if not arr or arr[-1] != curr.val:
                arr.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


