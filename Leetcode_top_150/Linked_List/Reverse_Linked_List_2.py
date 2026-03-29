# ======================================================
# REVERSE LINKED LIST II - ALL APPROACHES
# ======================================================

# Problem (LeetCode 92):
# Reverse a linked list from position left to right.
#
# Example:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Convert to Array)
# ------------------------------------------------------

class BruteForceSolution:
    def reverseBetween(self, head, left, right):

        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        # reverse subarray
        arr[left-1:right] = arr[left-1:right][::-1]

        # rebuild list
        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 2️⃣ Iterative (Head Insertion) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def reverseBetween(self, head, left, right):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Step 1: move prev to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: reverse using head insertion
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


# ------------------------------------------------------
# 3️⃣ Standard Reverse (Detach + Reverse + Attach)
# ------------------------------------------------------

class DetachReverseSolution:
    def reverseBetween(self, head, left, right):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        then = start.next

        # reverse
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next


# ------------------------------------------------------
# 4️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def reverseBetween(self, head, left, right):

        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor

        return last


# ------------------------------------------------------
# 5️⃣ Stack Based Approach
# ------------------------------------------------------

class StackSolution:
    def reverseBetween(self, head, left, right):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        stack = []
        curr = prev.next

        for _ in range(right - left + 1):
            stack.append(curr)
            curr = curr.next

        while stack:
            prev.next = stack.pop()
            prev = prev.next

        prev.next = curr

        return dummy.next


res = OptimalSolution().reverseBetween(head, 2, 4)
print_list(res)
