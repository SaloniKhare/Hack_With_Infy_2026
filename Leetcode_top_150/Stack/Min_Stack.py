# ======================================================
# MIN STACK - ALL APPROACHES
# ======================================================

# Problem (LeetCode 155):
# Design a stack that supports push, pop, top,
# and retrieving the minimum element in constant time.
#
# Functions:
# push(x)  -> Push element x onto stack
# pop()    -> Removes top element
# top()    -> Get top element
# getMin() -> Retrieve minimum element
#
# All operations must be O(1)


# ------------------------------------------------------
# 1️⃣ Brute Force (Recompute Min)
# ------------------------------------------------------

class BruteForceMinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)   # ❌ O(n)


# ------------------------------------------------------
# 2️⃣ Two Stack Approach (Most Important)
# ------------------------------------------------------

class TwoStackMinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# ------------------------------------------------------
# 3️⃣ Single Stack with Pair (Value, Min)
# ------------------------------------------------------

class PairMinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# ------------------------------------------------------
# 4️⃣ Optimized (Constant Space Trick)
# ------------------------------------------------------

class OptimizedMinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        else:
            if val < self.min_val:
                # store encoded value
                self.stack.append(2 * val - self.min_val)
                self.min_val = val
            else:
                self.stack.append(val)

    def pop(self):
        if not self.stack:
            return

        top = self.stack.pop()

        if top < self.min_val:
            # restore previous min
            self.min_val = 2 * self.min_val - top

    def top(self):
        top = self.stack[-1]

        if top < self.min_val:
            return self.min_val
        return top

    def getMin(self):
        return self.min_val


# ------------------------------------------------------
# 5️⃣ Pythonic (Using List + Min Tracking)
# ------------------------------------------------------

class PythonicMinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# ------------------------------------------------------
# Example
# ------------------------------------------------------

ms = TwoStackMinStack()

ms.push(3)
ms.push(5)
print("Min:", ms.getMin())  # 3

ms.push(2)
ms.push(1)
print("Min:", ms.getMin())  # 1

ms.pop()
print("Top:", ms.top())     # 2
print("Min:", ms.getMin())  # 2
