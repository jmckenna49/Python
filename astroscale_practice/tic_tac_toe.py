

class TicTacToe:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []
        
    def create_board(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(0)
            self.board.append(row)
        return self.board

    def make_a_move(self, row_pos, col_pos, shape):
        if self.board[row_pos][col_pos] == 0:
            self.board[row_pos][col_pos] = shape
            return self.board
        else:
            print("Not a valid position, this space is already occupied.")
            return
    def victory_condition(self):
        print(self.board)
        
        # Checking rows
        for row in self.board:
            # grab first cell as a reference
            first = row[0]
            if first == 0:
                continue
            winner = True
            # check each cell and make sure they're all equal
            for cell in row:
                if cell != first:
                    winner = False
                    break
            if winner:
                print(f"Victory! '{first}' wins!")
                return True

        # Checking columns
        for col in range(self.cols):
            first = self.board[0][col]
            if first == 0:
                continue
            winner = True
            # nested loop to fix columns and loop through rows in the column
            # makes sure the column is equal if not it breaks
            for r in range(self.rows):  # renamed to 'r'
                if self.board[r][col] != first:
                    winner = False
                    break
            if winner:
                print(f"Victory! '{first}' wins!")
                return True

        # Checking diagonals
        # Top-left to bottom-right
        first = self.board[0][0]
        # getting reference with first cell in board
        if first != 0:
            winner = True
            # checks first diagonal 0,0, 1,1, 2,2
            for i in range(self.rows):
                if self.board[i][i] != first:
                    winner = False
                    break
            if winner:
                print(f"Victory! '{first}' wins!")
                return True

        # Top-right to bottom-left
        first = self.board[0][self.cols - 1]
        # grabs board[0][2] as a reference point
        if first != 0:
            winner = True
            # proceeds to check [0][2], then [1][1], then [2][0]
            for i in range(self.rows):
                if self.board[i][self.cols - 1 - i] != first:
                    winner = False
                    break
            if winner:
                print(f"Victory! '{first}' wins!")
                return True
        # No winning condition
        return False

    def reset_board(self):
        self.board = []
        self.create_board()

if __name__ == "__main__":
    row = 3
    col = 3
    board = TicTacToe(rows=row, cols=col)
    print(board.create_board()) 
    print(board.make_a_move(0, 1, "x"))
    print(board.make_a_move(0, 0, "x"))
    print(board.make_a_move(0, 2, "x"))
        
    print(board.victory_condition())
    
    board.reset_board()
    print(board.board)