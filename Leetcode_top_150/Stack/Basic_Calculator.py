# ======================================================
# BASIC CALCULATOR - ALL APPROACHES
# ======================================================

# Problem (LeetCode 224):
# Given a string s representing an expression,
# evaluate this expression and return its value.
#
# Rules:
# - Supports +, -
# - Supports parentheses ()
# - No multiplication/division
#
# Example:
# Input: "1 + (2 - (3 + 4))"
# Output: -4


# ------------------------------------------------------
# 1️⃣ Stack Approach (Most Important)
# ------------------------------------------------------

class StackSolution:
    def calculate(self, s):

        stack = []
        result = 0
        number = 0
        sign = 1  # +1 or -1

        for ch in s:

            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * number
                number = 0
                result *= stack.pop()   # sign
                result += stack.pop()   # previous result

        result += sign * number
        return result


# ------------------------------------------------------
# 2️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def calculate(self, s):

        self.i = 0

        def helper():
            result = 0
            number = 0
            sign = 1

            while self.i < len(s):

                ch = s[self.i]

                if ch.isdigit():
                    number = number * 10 + int(ch)

                elif ch == '+':
                    result += sign * number
                    number = 0
                    sign = 1

                elif ch == '-':
                    result += sign * number
                    number = 0
                    sign = -1

                elif ch == '(':
                    self.i += 1
                    number = helper()

                elif ch == ')':
                    result += sign * number
                    return result

                self.i += 1

            return result + sign * number

        return helper()


# ------------------------------------------------------
# 3️⃣ Using eval (Not Recommended)
# ------------------------------------------------------

class EvalSolution:
    def calculate(self, s):
        return eval(s)


# ------------------------------------------------------
# 4️⃣ Two Stack (Operator + Operand)
# ------------------------------------------------------

class TwoStackSolution:
    def calculate(self, s):

        nums = []
        ops = []
        num = 0

        def apply():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()
            if op == '+':
                nums.append(a + b)
            else:
                nums.append(a - b)

        i = 0
        while i < len(s):

            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
                continue

            elif s[i] in "+-":
                while ops:
                    apply()
                ops.append(s[i])

            elif s[i] == '(':
                ops.append(s[i])

            elif s[i] == ')':
                while ops[-1] != '(':
                    apply()
                ops.pop()

            i += 1

        while ops:
            apply()

        return nums[0]


# ------------------------------------------------------
# 5️⃣ Pythonic (Using Stack + Sign)
# ------------------------------------------------------

class PythonicSolution:
    def calculate(self, s):

        res = 0
        num = 0
        sign = 1
        stack = []

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in '+-':
                res += sign * num
                num = 0
                sign = 1 if ch == '+' else -1

            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif ch == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        return res + sign * num


# ------------------------------------------------------
# Example
# ------------------------------------------------------

s = "1 + (2 - (3 + 4))"

print("Stack:", StackSolution().calculate(s))
print("Recursive:", RecursiveSolution().calculate(s))
print("Eval:", EvalSolution().calculate(s))
print("TwoStack:", TwoStackSolution().calculate(s))
print("Pythonic:", PythonicSolution().calculate(s))
