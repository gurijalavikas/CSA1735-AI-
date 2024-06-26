class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)
        self.cleaned_positions = []

    def clean(self):
        rows, cols = len(self.grid), len(self.grid[0])
        while True:
            x, y = self.position
            if self.grid[x][y] == 1:
                self.grid[x][y] = 0
                self.cleaned_positions.append(self.position)
                print(f"Cleaned position: {self.position}")

            next_position = self.get_next_position()
            if next_position is None:
                break
            self.position = next_position

    def get_next_position(self):
        rows, cols = len(self.grid), len(self.grid[0])
        x, y = self.position
        if y + 1 < cols:
            return (x, y + 1)
        elif x + 1 < rows:
            return (x + 1, 0)
        else:
            return None

    def display_grid(self):
        for row in self.grid:
            print(row)

if __name__ == "__main__":
    # 0 indicates a clean cell, 1 indicates a dirty cell
    grid = [
        [1, 0],
        [0, 1]
    ]

    vacuum = VacuumCleaner(grid)
    print("Initial grid state:")
    vacuum.display_grid()

    vacuum.clean()

    print("Final grid state:")
    vacuum.display_grid()

    print("Cleaned positions:")
    print(vacuum.cleaned_positions)
