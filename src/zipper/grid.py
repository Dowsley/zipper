"""Grid data structure for Zip puzzles"""

from typing import Optional


class Cell:
    """Represents a single cell in the grid"""

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.number: Optional[int] = None  # Checkpoint number (1, 2, 3, etc.)
        self.walls = {
            'N': False,  # Wall above (blocks movement up)
            'S': False,  # Wall below (blocks movement down)
            'E': False,  # Wall to right (blocks movement right)
            'W': False,  # Wall to left (blocks movement left)
        }
        self.visited = False

    def __repr__(self):
        return f"Cell({self.row},{self.col},num={self.number})"


class Grid:
    """Represents the puzzle grid"""

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.numbered_cells: dict[int, Cell] = {}

    def get_cell(self, row: int, col: int) -> Optional[Cell]:
        """Get cell at position, or None if out of bounds"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col]
        return None

    def set_number(self, row: int, col: int, number: int):
        """Set a checkpoint number at a cell"""
        cell = self.get_cell(row, col)
        if cell:
            cell.number = number
            self.numbered_cells[number] = cell

    def add_horizontal_wall(self, row: int, col: int):
        """
        Add a horizontal wall below cell at (row, col)
        This blocks movement between (row, col) and (row+1, col)
        """
        cell = self.get_cell(row, col)
        if cell:
            cell.walls['S'] = True

        cell_below = self.get_cell(row + 1, col)
        if cell_below:
            cell_below.walls['N'] = True

    def add_vertical_wall(self, row: int, col: int):
        """
        Add a vertical wall to the right of cell at (row, col)
        This blocks movement between (row, col) and (row, col+1)
        """
        cell = self.get_cell(row, col)
        if cell:
            cell.walls['E'] = True

        cell_right = self.get_cell(row, col + 1)
        if cell_right:
            cell_right.walls['W'] = True

    def get_neighbors(self, cell: Cell) -> list[tuple[Cell, str]]:
        """
        Get valid neighboring cells (not blocked by walls)
        Returns list of (neighbor_cell, direction) tuples
        """
        neighbors = []
        directions = [
            ('N', -1, 0),
            ('S', 1, 0),
            ('E', 0, 1),
            ('W', 0, -1),
        ]

        for direction, dr, dc in directions:
            if not cell.walls[direction]:
                neighbor = self.get_cell(cell.row + dr, cell.col + dc)
                if neighbor:
                    neighbors.append((neighbor, direction))

        return neighbors
