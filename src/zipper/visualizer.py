"""Visualization utilities for rendering grids"""

from .grid import Grid, Cell

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Unicode box-drawing characters
# Thin lines (normal borders)
H_LINE = "─"
V_LINE = "│"
TL_CORNER = "┌"
TR_CORNER = "┐"
BL_CORNER = "└"
BR_CORNER = "┘"
T_DOWN = "┬"
T_UP = "┴"
T_RIGHT = "├"
T_LEFT = "┤"
CROSS = "┼"

# Thick lines (walls)
H_WALL = "═"
V_WALL = "║"


def render_grid(grid: Grid, path: list[Cell] = None) -> str:
    """
    Render a grid with Unicode box-drawing characters

    Args:
        grid: The grid to render
        path: Optional list of cells representing the current path

    Returns:
        String representation of the grid
    """
    if path is None:
        path = []

    path_set = set((cell.row, cell.col) for cell in path)
    max_num = max(grid.numbered_cells.keys()) if grid.numbered_cells else 1
    cell_width = max(3, len(str(max_num)) + 2)

    lines = []

    for row_idx in range(grid.rows):
        if row_idx == 0:
            lines.append(_render_top_border(grid, row_idx, cell_width))
        else:
            lines.append(_render_middle_border(grid, row_idx, cell_width))
        lines.append(_render_cell_row(grid, row_idx, path_set, cell_width))

    lines.append(_render_bottom_border(grid, cell_width))

    return "\n".join(lines)


def _render_top_border(grid: Grid, row_idx: int, cell_width: int) -> str:
    """Render the top border of the grid"""
    parts = [TL_CORNER]

    for col_idx in range(grid.cols):
        parts.append(H_LINE * cell_width)

        if col_idx < grid.cols - 1:
            parts.append(T_DOWN)
        else:
            parts.append(TR_CORNER)

    return "".join(parts)


def _render_middle_border(grid: Grid, row_idx: int, cell_width: int) -> str:
    """Render a horizontal border between rows"""
    parts = [T_RIGHT]

    for col_idx in range(grid.cols):
        cell = grid.get_cell(row_idx - 1, col_idx)

        if cell and cell.walls['S']:
            parts.append(f"{RED}{H_WALL * cell_width}{RESET}")
        else:
            parts.append(H_LINE * cell_width)

        if col_idx < grid.cols - 1:
            parts.append(CROSS)
        else:
            parts.append(T_LEFT)

    return "".join(parts)


def _render_bottom_border(grid: Grid, cell_width: int) -> str:
    """Render the bottom border of the grid"""
    parts = [BL_CORNER]

    for col_idx in range(grid.cols):
        parts.append(H_LINE * cell_width)

        if col_idx < grid.cols - 1:
            parts.append(T_UP)
        else:
            parts.append(BR_CORNER)

    return "".join(parts)


def _render_cell_row(grid: Grid, row_idx: int, path_set: set, cell_width: int) -> str:
    """Render a row of cells with content"""
    parts = []

    for col_idx in range(grid.cols):
        cell = grid.get_cell(row_idx, col_idx)

        if col_idx == 0:
            parts.append(V_LINE)
        else:
            left_cell = grid.get_cell(row_idx, col_idx - 1)
            if left_cell and left_cell.walls['E']:
                parts.append(f"{RED}{V_WALL}{RESET}")
            else:
                parts.append(V_LINE)

        if cell:
            in_path = (row_idx, col_idx) in path_set
            if cell.number is not None:
                color = GREEN if in_path else BLUE
                content = f"{color}{cell.number}{RESET}"
                parts.append(content.center(cell_width + len(color) + len(RESET)))
            elif in_path:
                content = f"{GREEN}*{RESET}"
                parts.append(content.center(cell_width + len(GREEN) + len(RESET)))
            else:
                parts.append(" " * cell_width)

    parts.append(V_LINE)

    return "".join(parts)


def clear_screen():
    """Clear the terminal screen"""
    print("\033[2J\033[H", end="")


def move_cursor_home():
    """Move cursor to top-left without clearing"""
    print("\033[H", end="")
