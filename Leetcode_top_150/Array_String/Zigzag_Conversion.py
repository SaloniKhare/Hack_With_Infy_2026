# ======================================================
# ZIGZAG CONVERSION - ALL APPROACHES
# ======================================================

# Problem (LeetCode 6):
# Write the string in a zigzag pattern on numRows
# and then read line by line.


# ------------------------------------------------------
# 1️⃣ Brute Force (Matrix Simulation)
# ------------------------------------------------------

class MatrixSimulationSolution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        rows = [[""] * len(s) for _ in range(numRows)]

        r = 0
        c = 0
        down = True

        for ch in s:
            rows[r][c] = ch

            if down:
                if r == numRows - 1:
                    down = False
                    r -= 1
                    c += 1
                else:
                    r += 1
            else:
                if r == 0:
                    down = True
                    r += 1
                else:
                    r -= 1
                    c += 1

        ans = ""
        for row in rows:
            for ch in row:
                if ch:
                    ans += ch

        return ans


# ------------------------------------------------------
# 2️⃣ Row Builder (Most Common Solution)
# ------------------------------------------------------

class RowBuilderSolution:
    def convert(self, s: str, numRows: int):

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow = 0
        goingDown = False

        for c in s:

            rows[curRow] += c

            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown

            curRow += 1 if goingDown else -1

        return "".join(rows)


# ------------------------------------------------------
# 3️⃣ Direction Simulation
# ------------------------------------------------------

class DirectionSimulationSolution:
    def convert(self, s: str, numRows: int):

        if numRows == 1:
            return s

        rows = [""] * numRows
        i = 0
        direction = 1

        for ch in s:
            rows[i] += ch

            if i == 0:
                direction = 1
            elif i == numRows - 1:
                direction = -1

            i += direction

        return "".join(rows)


# ------------------------------------------------------
# 4️⃣ Mathematical Pattern Approach
# ------------------------------------------------------

class MathPatternSolution:
    def convert(self, s: str, numRows: int):

        if numRows == 1:
            return s

        result = ""
        cycle = 2 * numRows - 2

        for r in range(numRows):

            for j in range(r, len(s), cycle):
                result += s[j]

                second = j + cycle - 2 * r

                if r != 0 and r != numRows - 1 and second < len(s):
                    result += s[second]

        return result


# ------------------------------------------------------
# 5️⃣ Pythonic Row List
# ------------------------------------------------------

class PythonicSolution:
    def convert(self, s: str, numRows: int):

        if numRows == 1:
            return s

        rows = [''] * numRows
        index = 0
        step = 1

        for ch in s:
            rows[index] += ch

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(rows)
