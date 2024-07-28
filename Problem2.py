#Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = []
        rows = []
        squares = []
        
        for i in range(9):
            cols.append(set())
            rows.append(set())
            squares.append(set())
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # Calculate the index for the 3x3 sub-grid
                square_index = (r // 3) * 3 + (c // 3)

                # Check for duplicates
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[square_index]):
                    return False

                # Add the number to the corresponding row, column, and square
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[square_index].add(board[r][c])

        return True
