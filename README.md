# Zipper

A solver for LinkedIn's Zip puzzle game built with Python and managed with `uv`.

## Usage

**Display a puzzle:**
```bash
uv run main.py examples/puzzle1.json
```

**Solve a puzzle:**
```bash
uv run main.py examples/puzzle1.json --solve
```

**Animate the solving process (shows exploration and backtracking):**
```bash
uv run main.py examples/puzzle2.json --animate --delay 0.05
```

**Animate just the solution path:**
```bash
uv run main.py examples/puzzle1.json --animate-solution --delay 0.1
```

## Puzzle Input Format

Puzzles are defined in JSON:

```json
{
  "rows": 3,
  "cols": 3,
  "numbers": {
    "1": [0, 0],
    "2": [1, 1],
    "3": [2, 2]
  },
  "h_walls": [[1, 1]],
  "v_walls": [[0, 1]]
}
```

See `examples/README.md` for detailed format documentation.

## Visualization

The grid is rendered with:
- **Unicode box-drawing characters** for clean borders
- **Blue numbers** for checkpoints (1, 2, 3, ...)
- **Red thick lines** (═ ║) for walls
- **Green asterisks** (*) for the solution path

## Algorithm

Uses **DFS with backtracking** to find a Hamiltonian path through all cells:
- Visits numbered checkpoints in ascending order
- Respects wall constraints
- Backtracks on dead ends
- Typically solves 5×5 puzzles in <1ms, 8×8 puzzles in <2 seconds

## Roadmap

- [x] Input format and parser
- [x] Grid data structure
- [x] Terminal visualization
- [x] DFS backtracking solver
- [x] Animation mode
- [ ] Image input (OCR/Computer Vision)
