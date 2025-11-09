# Puzzle Input Format

```json
{
  "rows": 5,          // Grid height
  "cols": 5,          // Grid width
  "numbers": {        // Checkpoint cells (must be visited in order)
    "1": [0, 0],      // number: [row, col] (0-indexed)
    "2": [2, 2],
    "3": [4, 4]
  },
  "h_walls": [        // Horizontal walls (block vertical movement)
    [1, 2]            // [row, col] = wall between row 1 and row 2, at column 2
  ],
  "v_walls": [        // Vertical walls (block horizontal movement)
    [0, 2]            // [row, col] = wall between col 2 and col 3, at row 0
  ]
}
```

## Wall Coordinate System

Walls exist **between cells**, not in cells:

**Horizontal walls** (oriented horizontally, block vertical movement):
- Format: `[row, col]`
- Meaning: Wall between row `row` and row `row+1`, at column `col`
- Example: `[1, 2]` means you cannot move vertically between cells `(1,2)` and `(2,2)`

**Vertical walls** (oriented vertically, block horizontal movement):
- Format: `[row, col]`
- Meaning: Wall between column `col` and column `col+1`, at row `row`
- Example: `[0, 2]` means you cannot move horizontally between cells `(0,2)` and `(0,3)`
