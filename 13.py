import math

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.current_player = 'X'
        self.winner = None

    def print_board(self):
        print('-------------')
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                self.winner = self.board[i]
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                self.winner = self.board[i]
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.winner = self.board[2]
            return True
        # Check for draw
        if all(cell != ' ' for cell in self.board):
            self.winner = 'Draw'
            return True
        return False

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_empty_cells(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def minimax(self, depth, maximizing_player):
        if self.check_winner():
            if self.winner == 'X':
                return -10 + depth
            elif self.winner == 'O':
                return 10 - depth
            else:
                return 0

        if maximizing_player:
            max_eval = -math.inf
            for cell in self.get_empty_cells():
                self.board[cell] = 'O'
                eval = self.minimax(depth + 1, False)
                self.board[cell] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for cell in self.get_empty_cells():
                self.board[cell] = 'X'
                eval = self.minimax(depth + 1, True)
                self.board[cell] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_eval = -math.inf
        best_move = None
        for cell in self.get_empty_cells():
            self.board[cell] = 'O'
            eval = self.minimax(0, False)
            self.board[cell] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = cell
        return best_move

    def play(self):
        while not self.check_winner():
            self.print_board()
            if self.current_player == 'X':
                position = int(input('Enter your move (1-9): ')) - 1
                if 0 <= position <= 8:
                    if self.make_move(position):
                        self.switch_player()
                    else:
                        print('Invalid move! Try again.')
                else:
                    print('Invalid input! Enter a number between 1 and 9.')
            else:
                print("AI's turn...")
                best_move = self.find_best_move()
                self.make_move(best_move)
                self.switch_player()

        self.print_board()
        if self.winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"Player {self.winner} wins!")

# Start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
