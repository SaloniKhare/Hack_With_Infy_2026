# ======================================================
# MERGE TWO SORTED LISTS - ALL APPROACHES
# ======================================================

# Problem (LeetCode 21):
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes.
#
# Example:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Convert + Sort)
# ------------------------------------------------------

class BruteForceSolution:
    def mergeTwoLists(self, l1, l2):

        arr = []

        while l1:
            arr.append(l1.val)
            l1 = l1.next

        while l2:
            arr.append(l2.val)
            l2 = l2.next

        arr.sort()

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 2️⃣ Iterative (Two Pointer) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def mergeTwoLists(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:

            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        # attach remaining
        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next


# ------------------------------------------------------
# 3️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# ------------------------------------------------------
# 4️⃣ Using Dummy + Cleaner Code
# ------------------------------------------------------

class CleanerSolution:
    def mergeTwoLists(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next

            tail = tail.next

        tail.next = l1 or l2

        return dummy.next


# ------------------------------------------------------
# 5️⃣ In-Place Merge
# ------------------------------------------------------

class InPlaceSolution:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1

        head = l1

        while l1 and l2:

            prev = None

            while l1 and l1.val <= l2.val:
                prev = l1
                l1 = l1.next

            prev.next = l2
            l1, l2 = l2, l1

        return head


# ------------------------------------------------------
# Example
# ------------------------------------------------------

# l1 = 1 -> 2 -> 4
# l2 = 1 -> 3 -> 4

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

res = OptimalSolution().mergeTwoLists(l1, l2)
print_list(res)
