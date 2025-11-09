# Zipper

A solver for LinkedIn's Zip puzzle game

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

## Visualization

The grid is rendered with:
- **Unicode box-drawing characters** for clean borders
- **Blue numbers** for checkpoints (1, 2, 3, ...)
- **Red thick lines** (P Q) for walls
- **Green asterisks** (*) for the solution path (when solver is implemented)

## Roadmap

- [x] Input format and parser
- [x] Grid data structure
- [x] Terminal visualization
- [ ] Pathfinding solver algorithm
- [ ] Image input (OCR/Computer Vision)
