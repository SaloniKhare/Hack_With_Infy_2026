# ======================================================
# SIMPLIFY PATH - ALL APPROACHES
# ======================================================

# Problem (LeetCode 71):
# Given a string path representing an absolute Unix path,
# simplify it and return the canonical path.
#
# Rules:
# "."  -> current directory (ignore)
# ".." -> go to parent directory
# "//" -> multiple slashes treated as single
#
# Example:
# Input: "/a/./b/../../c/"
# Output: "/c"


# ------------------------------------------------------
# 1️⃣ Brute Force (Split + Rebuild)
# ------------------------------------------------------

class BruteForceSolution:
    def simplifyPath(self, path):

        parts = path.split("/")
        result = []

        for part in parts:

            if part == "" or part == ".":
                continue
            elif part == "..":
                if result:
                    result.pop()
            else:
                result.append(part)

        return "/" + "/".join(result)


# ------------------------------------------------------
# 2️⃣ Stack Approach (Most Important)
# ------------------------------------------------------

class StackSolution:
    def simplifyPath(self, path):

        stack = []

        for part in path.split("/"):

            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


# ------------------------------------------------------
# 3️⃣ Using Deque
# ------------------------------------------------------

from collections import deque

class DequeSolution:
    def simplifyPath(self, path):

        dq = deque()

        for part in path.split("/"):

            if part == "" or part == ".":
                continue
            elif part == "..":
                if dq:
                    dq.pop()
            else:
                dq.append(part)

        return "/" + "/".join(dq)


# ------------------------------------------------------
# 4️⃣ In-Place Simulation
# ------------------------------------------------------

class InPlaceSolution:
    def simplifyPath(self, path):

        stack = []
        curr = ""

        for ch in path + "/":

            if ch == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += ch

        return "/" + "/".join(stack)


# ------------------------------------------------------
# 5️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def simplifyPath(self, path):

        stack = []

        for part in filter(None, path.split("/")):

            if part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


# ------------------------------------------------------
# Example
# ------------------------------------------------------

path = "/a/./b/../../c/"

print("BruteForce:", BruteForceSolution().simplifyPath(path))
print("Stack:", StackSolution().simplifyPath(path))
print("Deque:", DequeSolution().simplifyPath(path))
print("InPlace:", InPlaceSolution().simplifyPath(path))
print("Pythonic:", PythonicSolution().simplifyPath(path))
