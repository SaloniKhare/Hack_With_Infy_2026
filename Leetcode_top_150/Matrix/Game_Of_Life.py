# ======================================================
# GAME OF LIFE - ALL APPROACHES
# ======================================================

# Problem (LeetCode 289):
# Given a 2D grid board where:
# 1 = live cell, 0 = dead cell
#
# Apply rules simultaneously:
# 1. Live cell with <2 live neighbors → dies
# 2. Live cell with 2 or 3 neighbors → lives
# 3. Live cell with >3 neighbors → dies
# 4. Dead cell with exactly 3 neighbors → becomes live
#
# Return next state (in-place).


# ------------------------------------------------------
# 1️⃣ Brute Force (Using Extra Matrix)
# ------------------------------------------------------

class BruteForceSolution:
    def gameOfLife(self, board):

        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),         (0,1),
            (1,-1), (1,0), (1,1)
        ]

        copy = [[board[i][j] for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):

                live_neighbors = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and copy[ni][nj] == 1:
                        live_neighbors += 1

                if copy[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 0
                else:
                    if live_neighbors == 3:
                        board[i][j] = 1


# ------------------------------------------------------
# 2️⃣ In-place (Using State Encoding)
# ------------------------------------------------------

class InPlaceSolution:
    def gameOfLife(self, board):

        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),         (0,1),
            (1,-1), (1,0), (1,1)
        ]

        # Encoding:
        # 0 → 0 (dead stays dead)
        # 1 → 1 (live stays live)
        # 1 → 0 (live → dead) = -1
        # 0 → 1 (dead → live) = 2

        for i in range(rows):
            for j in range(cols):

                live_neighbors = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and abs(board[ni][nj]) == 1:
                        live_neighbors += 1

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1   # live → dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2    # dead → live

        # Final update
        for i in range(rows):
            for j in range(cols):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0


# ------------------------------------------------------
# Example
# ------------------------------------------------------

board = [
 [0,1,0],
 [0,0,1],
 [1,1,1],
 [0,0,0]
]

BruteForceSolution().gameOfLife(board)
print(board)

board = [
 [0,1,0],
 [0,0,1],
 [1,1,1],
 [0,0,0]
]

InPlaceSolution().gameOfLife(board)
print(board)
