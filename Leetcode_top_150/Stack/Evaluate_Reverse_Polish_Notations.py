# ======================================================
# EVALUATE REVERSE POLISH NOTATION - ALL APPROACHES
# ======================================================

# Problem (LeetCode 150):
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators: +, -, *, /
# Each operand may be an integer.
# Division truncates toward zero.
#
# Example:
# Input: ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


# ------------------------------------------------------
# 1️⃣ Stack Approach (Most Important)
# ------------------------------------------------------

class StackSolution:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # truncate toward zero

        return stack[0]


# ------------------------------------------------------
# 2️⃣ Using Dictionary (Cleaner)
# ------------------------------------------------------

class DictSolution:
    def evalRPN(self, tokens):

        stack = []

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        for token in tokens:

            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]


# ------------------------------------------------------
# 3️⃣ Using eval (Not Recommended in Interviews)
# ------------------------------------------------------

class EvalSolution:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                expression = str(a) + token + str(b)
                stack.append(int(eval(expression)))
            else:
                stack.append(int(token))

        return stack[0]


# ------------------------------------------------------
# 4️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:
    def evalRPN(self, tokens):

        def helper():
            token = tokens.pop()

            if token not in "+-*/":
                return int(token)

            b = helper()
            a = helper()

            if token == '+':
                return a + b
            elif token == '-':
                return a - b
            elif token == '*':
                return a * b
            else:
                return int(a / b)

        return helper()


# ------------------------------------------------------
# 5️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            try:
                stack.append(int(token))
            except:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

        return stack[0]


# ------------------------------------------------------
# Example
# ------------------------------------------------------

tokens = ["2","1","+","3","*"]

print("Stack:", StackSolution().evalRPN(tokens.copy()))
print("Dict:", DictSolution().evalRPN(tokens.copy()))
print("Eval:", EvalSolution().evalRPN(tokens.copy()))
print("Recursive:", RecursiveSolution().evalRPN(tokens.copy()))
print("Pythonic:", PythonicSolution().evalRPN(tokens.copy()))
