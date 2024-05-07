def is_valid_sudoku(A):
    rows = [[False for i in range(len(A))] for j in range(len(A))]
    columns = [[False for i in range(len(A))] for j in range(len(A))]
    grids = [[False for i in range(len(A))] for j in range(len(A))]


    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == ".":
                continue
            else:
                num = int(A[i][j]) - 1
                grid = (i // 3) * 3 + j // 3

                if rows[i][num] or columns[j][num] or grids[grid][num]:
                    return 0
                else:
                    rows[i][num], columns[j][num], grids[grid][num] = True, True, True

    print("ROWS:")
    for row in rows:
        print(row)

    print("COLUMNS")
    for column in columns:
        print(column)

    print("GRIDS")
    for grid in grids:
        print(grid)

    return 1


if __name__ == "__main__":
    arr = [
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ]

    is_valid_sudoku(arr)