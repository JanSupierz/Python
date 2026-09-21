from z3 import *
import re

def build(grid)->tuple[Solver, list[list[ArithRef]], list[BoolRef]]:
    cells = [[Int(f'x{x}y{y}') for x in range(9)] for y in range(9)]
    flags = []

    s = SolverFor('QF_LIA')

    def add_implication(name, formula):
        flag = Bool(name)
        s.add(Implies(flag,formula))
        flags.append(flag)

    for y in range(9):
        for x in range(9):
            add_implication(f'incorrect domain ({x}, {y})', And(1 <= cells[x][y], cells[x][y] <= 9))

    for i in range(9):
        #distinc per column
        add_implication(f'conflict in row {i}', Distinct([cells[i][y] for y in range(9)]))

        #distinct per row
        add_implication(f'conflict in column {i}', Distinct([cells[x][i] for x in range(9)]))

    for block_x in range(3):
        for block_y in range(3):
            add_implication(f'conflict in block ({block_x}, {block_y})', Distinct([cells[x][y] for x in range(block_x * 3, block_x * 3 + 3) for y in range(block_y * 3, block_y * 3 + 3)]))

    for x in range(9):
        for y in range(9):
            if grid[x][y] != 0:
                add_implication(f'already assigned ({x}, {y}) = {grid[x][y]}', cells[x][y] == grid[x][y])

    return s, cells, flags

def minimize(s, probe, core_flags):
    cfs = list(core_flags)

    if probe in cfs:
        cfs.remove(probe)

    changed = True
    while changed:
        changed = False
        for flag in cfs[:]:
            trial = [cf for cf in cfs if cf is not flag]
            if s.check(*trial, probe) == unsat:
                cfs.remove(flag)
                changed = True
    return cfs

def why_not(sudoku, x, y, v):

    s, cells, flags = build(sudoku)

    probe = Bool(f'setting ({x}, {y}) to {v}')
    s.add(Implies(probe, cells[x][y]==v))

    result = s.check(*flags, probe)

    if result == sat:
        print(f'{v} is possible at ({x}, {y})')
        return
    elif result == unknown:
        print('not sat nor unsat?') 
        return

    mus = minimize(s, probe, s.unsat_core())
    print(f'{v} is impossible at ({x}, {y}):')
    format_mus(mus)

def format_mus(mus):
    rows, cols, blocks = {}, {}, {}

    for f in mus:
        name = str(f)
        m = re.match(r'conflict in row (\d+)$', name)
        if m:
            rows[int(m.group(1))] = []
            continue
        m = re.match(r'conflict in column (\d+)$', name)
        if m:
            cols[int(m.group(1))] = []
            continue
        m = re.match(r'conflict in block \((\d+), (\d+)\)$', name)
        if m:
            blocks[(int(m.group(1)), int(m.group(2)))] = []
            continue

    for f in mus:
        name = str(f)
        m = re.match(r'already assigned \((\d+), (\d+)\) = (\d+)$', name)
        if not m:
            continue
        row, col, val = map(int, m.groups())

        if row in rows:
            rows[row].append(name)
        if col in cols:
            cols[col].append(name)
        if (row // 3, col // 3) in blocks:
            blocks[(row // 3, col // 3)].append(name)

    for i in sorted(rows):
        if rows[i]:
            print(f'  conflict in row {i}')
            for c in rows[i]:
                print(f'      {c}')
    for i in sorted(cols):
        if cols[i]:
            print(f'  conflict in column {i}')
            for c in cols[i]:
                print(f'      {c}')
    for key in sorted(blocks):
        if blocks[key]:
            print(f'  conflict in block {key}')
            for c in blocks[key]:
                print(f'      {c}')

def solve_sudoku(grid):
    s, cells, flags = build(grid)

    if s.check(*flags) == sat:
        solution = [[s.model().eval(cells[x][y]).as_long() for y in range(9)] for x in range(9)]

        for r, row in enumerate(solution):
            print(  " ".join(str(row[i])     for i in range(3)) + " | " +
                    " ".join(str(row[i + 3]) for i in range(3)) + " | " +
                    " ".join(str(row[i + 6]) for i in range(3)))
            
            if(r%3 == 2 and r != 8):
                print("------+-------+------")
    else:
        print('No solution found.')

def main():
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

    why_not(grid, 0, 0, 8)
    print()
    why_not(grid, 1, 0, 9)
    print()
    why_not(grid, 2, 0, 2)
    print()
    solve_sudoku(grid)

if __name__ == "__main__":
    main()