"""DFS backtracking solver for Zip puzzles"""

from typing import Optional, Iterator
from .grid import Grid, Cell


def solve(grid: Grid) -> Optional[list[Cell]]:
    """
    Find a Hamiltonian path through the grid visiting all cells.
    Path must go through numbered checkpoints in ascending order.

    Returns the complete path if solution exists, None otherwise.
    """
    if not grid.numbered_cells:
        return None

    start_cell = grid.numbered_cells[1]
    total_cells = grid.rows * grid.cols
    max_checkpoint = max(grid.numbered_cells.keys())

    path = []
    visited = set()

    if _dfs_backtrack(grid, start_cell, path, visited, 1, max_checkpoint, total_cells):
        return path

    return None


def solve_with_steps(grid: Grid) -> Iterator[list[Cell]]:
    """
    Generator that yields intermediate path states during solving.
    Useful for visualization of the solving process.
    """
    if not grid.numbered_cells:
        return

    start_cell = grid.numbered_cells[1]
    total_cells = grid.rows * grid.cols
    max_checkpoint = max(grid.numbered_cells.keys())

    path = []
    visited = set()

    yield from _dfs_backtrack_with_steps(
        grid, start_cell, path, visited, 1, max_checkpoint, total_cells
    )


def _dfs_backtrack(
    grid: Grid,
    cell: Cell,
    path: list[Cell],
    visited: set[tuple[int, int]],
    next_checkpoint: int,
    final_checkpoint: int,
    total_cells: int
) -> bool:
    """
    Recursive DFS with backtracking.

    Returns True if a valid path is found from this state, False otherwise.
    """
    cell_pos = (cell.row, cell.col)

    if cell.number is not None and cell.number != next_checkpoint:
        return False

    visited.add(cell_pos)
    path.append(cell)

    if cell.number is not None:
        next_checkpoint = cell.number + 1

    if len(path) == total_cells and cell.number == final_checkpoint:
        return True

    for neighbor, _ in grid.get_neighbors(cell):
        neighbor_pos = (neighbor.row, neighbor.col)

        if neighbor_pos not in visited:
            if _dfs_backtrack(grid, neighbor, path, visited, next_checkpoint, final_checkpoint, total_cells):
                return True

    visited.remove(cell_pos)
    path.pop()
    return False


def _dfs_backtrack_with_steps(
    grid: Grid,
    cell: Cell,
    path: list[Cell],
    visited: set[tuple[int, int]],
    next_checkpoint: int,
    final_checkpoint: int,
    total_cells: int
) -> Iterator[list[Cell]]:
    """
    Recursive DFS with backtracking that yields intermediate states.
    """
    cell_pos = (cell.row, cell.col)

    if cell.number is not None and cell.number != next_checkpoint:
        return

    visited.add(cell_pos)
    path.append(cell)

    yield path.copy()

    if cell.number is not None:
        next_checkpoint = cell.number + 1

    if len(path) == total_cells and cell.number == final_checkpoint:
        return

    for neighbor, _ in grid.get_neighbors(cell):
        neighbor_pos = (neighbor.row, neighbor.col)

        if neighbor_pos not in visited:
            yield from _dfs_backtrack_with_steps(
                grid, neighbor, path, visited, next_checkpoint, final_checkpoint, total_cells
            )

    visited.remove(cell_pos)
    path.pop()
