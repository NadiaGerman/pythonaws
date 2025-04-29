import random

class TreasureHunt:
    def __init__(self):
        self.grid_size = 10
        self.max_moves = 20
        self.treasures_needed = 5
        self.traps_count = 5

        self.treasures_found = 0
        self.moves_made = 0
        self.player_position = [0, 0]

        self.grid = [['?' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.revealed = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.treasures = set()
        self.traps = set()
        self.place_treasures_and_traps()

    def place_treasures_and_traps(self):
        while len(self.treasures) < self.treasures_needed:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if (row, col) != (0, 0):
                self.treasures.add((row, col))

        while len(self.traps) < self.traps_count:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if (row, col) != (0, 0) and (row, col) not in self.treasures:
                self.traps.add((row, col))

    def render_board(self):
        for r in range(self.grid_size):
            row = ''
            for c in range(self.grid_size):
                if [r, c] == self.player_position:
                    row += 'P '
                elif self.revealed[r][c]:
                    if (r, c) in self.treasures:
                        row += 'T '
                    elif (r, c) in self.traps:
                        row += 'X '
                    else:
                        row += '. '
                else:
                    row += '? '
            print(row)
        print()

    def move_player(self, direction):
        row, col = self.player_position
        if direction == 'W' and row > 0:
            row -= 1
        elif direction == 'S' and row < self.grid_size - 1:
            row += 1
        elif direction == 'A' and col > 0:
            col -= 1
        elif direction == 'D' and col < self.grid_size - 1:
            col += 1
        else:
            print("Invalid move. You hit a wall.")
            return

        self.player_position = [row, col]
        self.revealed[row][col] = True
        self.moves_made += 1

        if (row, col) in self.treasures:
            print(" You found a treasure!")
            self.treasures_found += 1
            self.treasures.remove((row, col))
        elif (row, col) in self.traps:
            print(" You fell into a trap! Game over.")
            return 'lose'

        if self.treasures_found == self.treasures_needed:
            print(" You found all treasures! You win!")
            return 'win'

        if self.moves_made >= self.max_moves:
            print(" Out of moves! Game over.")
            return 'lose'

        return 'continue'

    def start_game(self):
        print("Welcome to Treasure Hunt!")
        print("Find all treasures (T) without hitting traps (X)!")
        print("Move using W (up), A (left), S (down), D (right)")
        print(f"You need to find {self.treasures_needed} treasures in {self.max_moves} moves.")
        print("Let's begin!\n")

        while True:
            self.render_board()
            move = input("Your move (W/A/S/D): ").strip().upper()
            if move in ['W', 'A', 'S', 'D']:
                result = self.move_player(move)
                if result in ['win', 'lose']:
                    self.render_board()
                    break
            else:
                print(" Invalid input. Use W, A, S, or D.")

# Run the game
if __name__ == "__main__":
    game = TreasureHunt()
    game.start_game()
