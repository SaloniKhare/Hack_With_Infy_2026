# ======================================================
# LINKED LIST CYCLE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 141):
# Given head of a linked list, determine if the list has a cycle.
#
# A cycle exists if some node can be reached again by continuously following next pointers.
#
# Example:
# Input: head = [3,2,0,-4], pos = 1 (cycle at index 1)
# Output: True


# ------------------------------------------------------
# Definition for singly-linked list
# ------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Visited Set)
# ------------------------------------------------------

class BruteForceSolution:
    def hasCycle(self, head):

        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False


# ------------------------------------------------------
# 2️⃣ Floyd’s Cycle Detection (Tortoise & Hare) ⭐ MOST IMPORTANT
# ------------------------------------------------------

class OptimalSolution:
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# ------------------------------------------------------
# 3️⃣ Marking Nodes (Modify Values) ❌ Not Recommended
# ------------------------------------------------------

class ModifySolution:
    def hasCycle(self, head):

        while head:
            if head.val == float('inf'):
                return True

            head.val = float('inf')
            head = head.next

        return False


# ------------------------------------------------------
# 4️⃣ Using Dictionary
# ------------------------------------------------------

class DictSolution:
    def hasCycle(self, head):

        visited = {}

        while head:
            if head in visited:
                return True
            visited[head] = True
            head = head.next

        return False


# ------------------------------------------------------
# 5️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def hasCycle(self, head, visited=None):

        if visited is None:
            visited = set()

        if not head:
            return False

        if head in visited:
            return True

        visited.add(head)

        return self.hasCycle(head.next, visited)


# ------------------------------------------------------
# Example
# ------------------------------------------------------

# Creating a cycle manually:
# 3 -> 2 -> 0 -> -4
#      ^         |
#      |_________|

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle here

print("BruteForce:", BruteForceSolution().hasCycle(node1))
print("Optimal:", OptimalSolution().hasCycle(node1))
print("Modify:", ModifySolution().hasCycle(node1))
print("Dict:", DictSolution().hasCycle(node1))
print("Recursive:", RecursiveSolution().hasCycle(node1))
