#!/usr/bin/env python3
"""Main entry point for the Zip puzzle solver"""

import json
import sys

from zipper import load_puzzle, render_grid


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <puzzle_file>")
        print("\nExample:")
        print("  python main.py examples/puzzle1.json")
        sys.exit(1)

    puzzle_file = sys.argv[1]

    try:
        grid = load_puzzle(puzzle_file)

        print(f"\nLoaded puzzle from: {puzzle_file}")
        print(f"Grid size: {grid.rows}x{grid.cols}")
        print(f"Checkpoints: {sorted(grid.numbered_cells.keys())}\n")
        print(render_grid(grid))
        print() # newline

    except FileNotFoundError:
        print(f"Error: File '{puzzle_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{puzzle_file}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
