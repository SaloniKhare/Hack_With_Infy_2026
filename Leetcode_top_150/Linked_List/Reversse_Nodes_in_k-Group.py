# ======================================================
# REVERSE NODES IN K-GROUP - ALL APPROACHES
# ======================================================

# Problem (LeetCode 25):
# Given a linked list, reverse nodes in groups of k.
# If remaining nodes < k, leave them as is.
#
# Example:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]


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
    def reverseKGroup(self, head, k):

        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        # reverse in chunks
        for i in range(0, len(arr), k):
            if i + k <= len(arr):
                arr[i:i+k] = arr[i:i+k][::-1]

        # rebuild list
        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 2️⃣ Iterative (Most Important)
# ------------------------------------------------------

class OptimalSolution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:

            # check if k nodes exist
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # reverse group
            prev = group_next
            curr = prev_group.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # reconnect
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp


# ------------------------------------------------------
# 3️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def reverseKGroup(self, head, k):

        count = 0
        curr = head

        # check if enough nodes
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        # reverse first k nodes
        prev = None
        curr = head

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # recursive call
        head.next = self.reverseKGroup(curr, k)

        return prev


# ------------------------------------------------------
# 4️⃣ Stack Based Approach
# ------------------------------------------------------

class StackSolution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:

            stack = []
            curr = prev.next

            for _ in range(k):
                if not curr:
                    return dummy.next
                stack.append(curr)
                curr = curr.next

            while stack:
                prev.next = stack.pop()
                prev = prev.next

            prev.next = curr


# ------------------------------------------------------
# 5️⃣ In-Place (Head Insertion Variation)
# ------------------------------------------------------

class HeadInsertionSolution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:

            tail = prev

            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            curr = prev.next

            for _ in range(k - 1):
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp

            prev = curr
