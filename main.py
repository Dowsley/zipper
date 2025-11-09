#!/usr/bin/env python3
"""Main entry point for the Zip puzzle solver"""

import argparse
import json
import sys
import time

from zipper import load_puzzle, render_grid, solve, solve_with_steps
from zipper.visualizer import clear_screen, move_cursor_home


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Zip puzzle solver")
    parser.add_argument("puzzle_file", help="Path to puzzle JSON file")
    parser.add_argument("--solve", action="store_true", help="Solve the puzzle")
    parser.add_argument("--animate", action="store_true", help="Animate the solving process (shows exploration)")
    parser.add_argument("--animate-solution", action="store_true", help="Animate the final solution path")
    parser.add_argument("--delay", type=float, default=0.05, help="Animation delay in seconds (default: 0.05)")

    args = parser.parse_args()

    if args.animate and args.animate_solution:
        print("Error: Cannot use both --animate and --animate-solution")
        sys.exit(1)

    try:
        grid = load_puzzle(args.puzzle_file)

        print(f"\nLoaded puzzle from: {args.puzzle_file}")
        print(f"Grid size: {grid.rows}x{grid.cols}")
        print(f"Checkpoints: {sorted(grid.numbered_cells.keys())}\n")

        if args.animate:
            animate_solving(grid, args.delay)
        elif args.animate_solution:
            animate_solution(grid, args.delay)
        elif args.solve:
            solve_and_display(grid)
        else:
            print(render_grid(grid))
            print()

    except FileNotFoundError:
        print(f"Error: File '{args.puzzle_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{args.puzzle_file}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def solve_and_display(grid):
    """Solve the puzzle and display the result"""
    print("Solving...\n")
    start_time = time.time()

    solution = solve(grid)
    elapsed = time.time() - start_time

    if solution:
        print(f"Solution found in {elapsed:.3f} seconds!")
        print(f"Path length: {len(solution)} cells\n")
        print(render_grid(grid, solution))
        print()
    else:
        print(f"No solution found (searched for {elapsed:.3f} seconds)")


def animate_solving(grid, delay):
    """Animate the solving process step by step"""
    clear_screen()
    print(f"Solving with animation (delay: {delay}s)...\n")

    for path in solve_with_steps(grid):
        move_cursor_home()
        print(render_grid(grid, path))
        time.sleep(delay)

    print(f"\nSolution found! Path length: {len(path)} cells")


def animate_solution(grid, delay):
    """Animate just the final solution path being drawn"""
    print("Solving...\n")
    start_time = time.time()

    solution = solve(grid)
    elapsed = time.time() - start_time

    if not solution:
        print(f"No solution found (searched for {elapsed:.3f} seconds)")
        return

    print(f"Solution found in {elapsed:.3f} seconds!")
    print(f"Animating solution (delay: {delay}s)...\n")
    time.sleep(1)

    clear_screen()

    for i in range(1, len(solution) + 1):
        move_cursor_home()
        partial_path = solution[:i]
        print(render_grid(grid, partial_path))
        time.sleep(delay)

    print(f"\nComplete! Path length: {len(solution)} cells")


if __name__ == "__main__":
    main()
