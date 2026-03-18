# ======================================================
# VALID SUDOKU - ALL APPROACHES
# ======================================================

# Problem (LeetCode 36):
# Determine if a 9x9 Sudoku board is valid.
# Rules:
# 1. Each row must contain digits 1-9 without repetition
# 2. Each column must contain digits 1-9 without repetition
# 3. Each 3x3 sub-box must contain digits 1-9 without repetition
#
# Note:
# - The board may be partially filled ('.' means empty)


# ------------------------------------------------------
# 1️⃣ Brute Force (Check Row, Col, Box separately)
# ------------------------------------------------------

class BruteForceSolution:
    def isValidSudoku(self, board):

        # Check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # Check columns
        for j in range(9):
            seen = set()
            for i in range(9):
                val = board[i][j]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row+i][box_col+j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True


# ------------------------------------------------------
# 2️⃣ Hash Set (Single Pass)
# ------------------------------------------------------

class HashSetSolution:
    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                if val == '.':
                    continue

                box_idx = (i // 3) * 3 + (j // 3)

                if (val in rows[i] or
                    val in cols[j] or
                    val in boxes[box_idx]):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)

        return True


# ------------------------------------------------------
# 3️⃣ Bitmask Optimization (Advanced)
# ------------------------------------------------------

class BitmaskSolution:
    def isValidSudoku(self, board):

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                if val == '.':
                    continue

                num = int(val) - 1
                mask = 1 << num

                box_idx = (i // 3) * 3 + (j // 3)

                if (rows[i] & mask or
                    cols[j] & mask or
                    boxes[box_idx] & mask):
                    return False

                rows[i] |= mask
                cols[j] |= mask
                boxes[box_idx] |= mask

        return True

print(BitmaskSolution().isValidSudoku(board))
