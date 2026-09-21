## Welcome to my Python playground!

# Here you can find some of my test projects:
- guess.py
    (try guessing the number --- Pro tip: use binary search)

- rps.py
    (implementation of windows defender, testing #tkinter)

- dijkstra.py
    (playing with graph generation (#networkx), implementing the dijkstra algorithm, and exploring gifs)

- sudoku.py
    (using Z3 to solve a sudoku, explaining why a value can't be placed)

## Highlight from sudoku

Initial sudoku (0 means empty):

```python
    grid = [
        [0,9,0, 0,0,6, 0,0,0],
        [0,0,0, 0,2,0, 7,0,0],
        [0,0,0, 0,7,0, 9,0,0],

        [0,6,0, 5,0,0, 0,0,4],
        [1,0,0, 0,0,0, 0,6,0],
        [0,0,0, 8,0,0, 0,0,0],

        [7,0,0, 0,0,4, 0,0,0],
        [3,0,0, 0,0,0, 8,0,0],
        [0,0,0, 9,0,0, 0,0,0]
    ]
```

Checking:
```python
why_not(grid, 0, 0, 8)
```
```text
8 is possible at (0, 0)
```
```python
    why_not(grid, 1, 0, 9)
```
```text
9 is impossible at (1, 0):
  conflict in block (0, 0)
      already assigned (0, 1) = 9
```
```python
why_not(grid, 2, 0, 2)
```
```text
2 is impossible at (2, 0):
  conflict in row 0
      already assigned (0, 5) = 6
      already assigned (0, 1) = 9
  conflict in row 3
      already assigned (3, 3) = 5
      already assigned (3, 1) = 6
      already assigned (3, 8) = 4
  conflict in row 4
      already assigned (4, 7) = 6
      already assigned (4, 0) = 1
  conflict in row 8
      already assigned (8, 3) = 9
  conflict in column 0
      already assigned (7, 0) = 3
      already assigned (6, 0) = 7
      already assigned (4, 0) = 1
  conflict in column 1
      already assigned (0, 1) = 9
      already assigned (3, 1) = 6
  conflict in column 3
      already assigned (3, 3) = 5
      already assigned (8, 3) = 9
      already assigned (5, 3) = 8
  conflict in column 4
      already assigned (2, 4) = 7
      already assigned (1, 4) = 2
  conflict in column 6
      already assigned (7, 6) = 8
      already assigned (2, 6) = 9
  conflict in block (0, 1)
      already assigned (0, 5) = 6
      already assigned (2, 4) = 7
      already assigned (1, 4) = 2
  conflict in block (1, 0)
      already assigned (3, 1) = 6
      already assigned (4, 0) = 1
  conflict in block (1, 1)
      already assigned (3, 3) = 5
      already assigned (5, 3) = 8
  conflict in block (2, 0)
      already assigned (7, 0) = 3
      already assigned (6, 0) = 7
  conflict in block (2, 1)
      already assigned (6, 5) = 4
      already assigned (8, 3) = 9
```
```puthon
    solve_sudoku(grid)
```
```text
8 9 7 | 3 5 6 | 4 2 1
6 1 5 | 4 2 9 | 7 3 8
4 3 2 | 1 7 8 | 9 5 6
------+-------+------
2 6 3 | 5 9 7 | 1 8 4
1 7 8 | 2 4 3 | 5 6 9
9 5 4 | 8 6 1 | 2 7 3
------+-------+------
7 2 9 | 6 8 4 | 3 1 5
3 4 6 | 7 1 5 | 8 9 2
5 8 1 | 9 3 2 | 6 4 7
```