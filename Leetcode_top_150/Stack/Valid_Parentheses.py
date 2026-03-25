# ======================================================
# VALID PARENTHESES - ALL APPROACHES
# ======================================================

# Problem (LeetCode 20):
# Given a string s containing just the characters:
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# A string is valid if:
# 1. Open brackets are closed by the same type
# 2. Open brackets are closed in correct order
#
# Example:
# Input: "()[]{}"
# Output: True


# ------------------------------------------------------
# 1️⃣ Brute Force (Replace Until Stable)
# ------------------------------------------------------

class BruteForceSolution:
    def isValid(self, s):

        prev = None

        while prev != s:
            prev = s
            s = s.replace("()", "").replace("{}", "").replace("[]", "")

        return s == ""


# ------------------------------------------------------
# 2️⃣ Stack (Most Important)
# ------------------------------------------------------

class StackSolution:
    def isValid(self, s):

        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


# ------------------------------------------------------
# 3️⃣ Stack (Using Only One Dict)
# ------------------------------------------------------

class CleanStackSolution:
    def isValid(self, s):

        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for ch in s:

            if ch in pairs:
                stack.append(ch)
            else:
                if not stack or pairs[stack.pop()] != ch:
                    return False

        return not stack


# ------------------------------------------------------
# 4️⃣ Using List as Stack (Pythonic)
# ------------------------------------------------------

class PythonicSolution:
    def isValid(self, s):

        stack = []

        for ch in s:

            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if (top == '(' and ch != ')') or \
                   (top == '{' and ch != '}') or \
                   (top == '[' and ch != ']'):
                    return False

        return not stack


# ------------------------------------------------------
# 5️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def isValid(self, s):

        if not s:
            return True

        for i in range(len(s) - 1):
            pair = s[i:i+2]

            if pair in ["()", "{}", "[]"]:
                return self.isValid(s[:i] + s[i+2:])

        return False


# ------------------------------------------------------
# Example
# ------------------------------------------------------

s = "()[]{}"

print("BruteForce:", BruteForceSolution().isValid(s))
print("Stack:", StackSolution().isValid(s))
print("CleanStack:", CleanStackSolution().isValid(s))
print("Pythonic:", PythonicSolution().isValid(s))
print("Recursive:", RecursiveSolution().isValid(s))
