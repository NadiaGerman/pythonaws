# TicTacToe.py — A complete two-player console game with win/draw check

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = None
        self.player1 = None
        self.player2 = None
        self.symbols = {}

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")

    def choose_symbols(self):
        print("\n--- Player Setup ---")
        self.player1 = input("Enter name for Player 1: ").strip()
        self.player2 = input("Enter name for Player 2: ").strip()
        while True:
            symbol = input(f"{self.player1}, do you want to be X or O? ").strip().upper()
            if symbol in ['X', 'O']:
                self.symbols[self.player1] = symbol
                self.symbols[self.player2] = 'O' if symbol == 'X' else 'X'
                self.current_player = self.player1
                break
            else:
                print("Invalid choice. Please choose X or O.")

    def make_move(self, position):
        if 1 <= position <= 9 and self.board[position - 1] == ' ':
            self.board[position - 1] = self.symbols[self.current_player]
            return True
        return False

    def check_winner(self):
        s = self.symbols[self.current_player]
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[i] == s for i in pattern) for pattern in win_patterns)

    def check_draw(self):
        return all(cell != ' ' for cell in self.board)

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def reset_board(self):
        self.board = [' '] * 9

    def play_game(self):
        print("\n🎮 Game Starting!")
        print("The board has positions 1 to 9 like this:")
        print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 \n")

        self.choose_symbols()

        game_running = True
        while game_running:
            self.display_board()
            try:
                position = int(input(f"{self.current_player}'s turn ({self.symbols[self.current_player]}). Enter position (1–9): "))
                if self.make_move(position):
                    if self.check_winner():
                        self.display_board()
                        print(f" {self.current_player} wins! ")
                        game_running = False
                    elif self.check_draw():
                        self.display_board()
                        print("🤝 It's a draw!")
                        game_running = False
                    else:
                        self.switch_player()
                else:
                    print(" Invalid move. Position already taken or out of range.")
            except ValueError:
                print(" Invalid input. Please enter a number between 1 and 9.")

        if input("Play again? (y/n): ").strip().lower() == 'y':
            self.reset_board()
            self.play_game()


def main_menu():
    while True:
        print("=" * 50)
        print("  Welcome to Tic Tac Toe!".center(50))
        print("=" * 50)
        print("1. Start New Game")
        print("2. Quit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            game = TicTacToe()
            game.play_game()
        elif choice == '2':
            print(" Thanks for playing! Goodbye.")
            break
        else:
            print(" Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main_menu()
