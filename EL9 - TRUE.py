class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.memo = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] != 1

    def find_path(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        if row == self.rows - 1 and col == self.cols - 1:
            return True
        if self.memo[row][col] != -1:
            return self.memo[row][col]

        self.grid[row][col] = 1  

        if self.find_path(row + 1, col) or self.find_path(row, col + 1):
            self.memo[row][col] = True
            return True

        self.memo[row][col] = False
        return False

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

robot = Robot(grid)
print(robot.find_path(0, 0)) 
