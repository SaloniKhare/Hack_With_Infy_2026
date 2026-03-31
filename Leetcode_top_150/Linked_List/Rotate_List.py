# ======================================================
# ROTATE LIST - ALL APPROACHES
# ======================================================

# Problem (LeetCode 61):
# Given the head of a linked list, rotate the list to the right by k places.
#
# Example:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Rotate One by One)
# ------------------------------------------------------

class BruteForceSolution:
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head

        # get length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        k %= n

        for _ in range(k):
            prev = None
            curr = head

            while curr.next:
                prev = curr
                curr = curr.next

            prev.next = None
            curr.next = head
            head = curr

        return head


# ------------------------------------------------------
# 2️⃣ Optimal (Circular Linked List) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def rotateRight(self, head, k):

        if not head or not head.next or k == 0:
            return head

        # Step 1: find length & tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # Step 2: make circular
        tail.next = head

        # Step 3: find new head
        k %= n
        steps_to_new_head = n - k

        new_tail = tail
        while steps_to_new_head:
            new_tail = new_tail.next
            steps_to_new_head -= 1

        new_head = new_tail.next

        # break circle
        new_tail.next = None

        return new_head


# ------------------------------------------------------
# 3️⃣ Two Pointer Approach
# ------------------------------------------------------

class TwoPointerSolution:
    def rotateRight(self, head, k):

        if not head:
            return head

        # length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        k %= n
        if k == 0:
            return head

        fast = head
        slow = head

        # move fast k steps
        for _ in range(k):
            fast = fast.next if fast.next else head

        while fast.next:
            fast = fast.next
            slow = slow.next

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head


# ------------------------------------------------------
# 4️⃣ Using Array Conversion
# ------------------------------------------------------

class ArraySolution:
    def rotateRight(self, head, k):

        if not head:
            return head

        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        k %= n

        arr = arr[-k:] + arr[:-k]

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


# ------------------------------------------------------
# 5️⃣ Stack Based Approach
# ------------------------------------------------------

class StackSolution:
    def rotateRight(self, head, k):

        if not head:
            return head

        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        n = len(stack)
        k %= n

        if k == 0:
            return head

        new_head = stack[-k]
        new_tail = stack[-k - 1]

        new_tail.next = None
        stack[-1].next = head

        return new_head


# ------------------------------------------------------
# Example
# ------------------------------------------------------

# 1 -> 2 -> 3 -> 4 -> 5
# k = 2 → 4 -> 5 -> 1 -> 2 -> 3

head = ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4,
        ListNode(5)))))

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

res = OptimalSolution().rotateRight(head, 2)
print_list(res)
