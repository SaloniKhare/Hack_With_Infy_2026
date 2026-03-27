# ======================================================
# ADD TWO NUMBERS (LINKED LIST) - ALL APPROACHES
# ======================================================

# Problem (LeetCode 2):
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each node contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# Example:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Convert to Integer)
# ------------------------------------------------------

class BruteForceSolution:
    def addTwoNumbers(self, l1, l2):

        def toNumber(node):
            num = 0
            place = 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num

        n1 = toNumber(l1)
        n2 = toNumber(l2)

        total = n1 + n2

        # convert back to linked list
        dummy = ListNode()
        curr = dummy

        if total == 0:
            return ListNode(0)

        while total:
            curr.next = ListNode(total % 10)
            total //= 10
            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 2️⃣ Iterative (Carry Handling) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ------------------------------------------------------
# 3️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def addTwoNumbers(self, l1, l2, carry=0):

        if not l1 and not l2 and not carry:
            return None

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10

        node = ListNode(total % 10)

        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None

        node.next = self.addTwoNumbers(next1, next2, carry)

        return node


# ------------------------------------------------------
# 4️⃣ Using Stack (Forward Order Variation)
# ------------------------------------------------------

class StackSolution:
    def addTwoNumbers(self, l1, l2):

        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while s1 or s2 or carry:

            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            node = ListNode(total % 10)
            node.next = head
            head = node

        return head


# ------------------------------------------------------
# 5️⃣ In-Place Modification
# ------------------------------------------------------

class InPlaceSolution:
    def addTwoNumbers(self, l1, l2):

        head = l1
        carry = 0

        while l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            if l1:
                l1.val = total % 10
                prev = l1
                l1 = l1.next
            else:
                prev.next = ListNode(total % 10)
                prev = prev.next

            if l2:
                l2 = l2.next

        if carry:
            prev.next = ListNode(carry)

        return head
