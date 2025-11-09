"""Parser for reading puzzle input files"""

import json
from pathlib import Path
from .grid import Grid


def load_puzzle(filepath: str | Path) -> Grid:
    """
    Load a puzzle from a JSON file

    Args:
        filepath: Path to the JSON puzzle file

    Returns:
        Grid object with the puzzle loaded
    """
    with open(filepath, 'r') as f:
        data = json.load(f)

    grid = Grid(rows=data['rows'], cols=data['cols'])

    for number_str, position in data['numbers'].items():
        number = int(number_str)
        row, col = position
        grid.set_number(row, col, number)

    # Add horizontal walls (between rows, blocking vertical movement)
    # Format: [row, col] means wall between row and row+1 at column col
    for wall in data.get('h_walls', []):
        row, col = wall
        grid.add_horizontal_wall(row, col)

    # Add vertical walls (between columns, blocking horizontal movement)
    # Format: [row, col] means wall between col and col+1 at row row
    for wall in data.get('v_walls', []):
        row, col = wall
        grid.add_vertical_wall(row, col)

    return grid
