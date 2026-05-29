from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    grid = []
    for j in range(cols):       # outer loop
        row = []
        for i in range(rows):   # inner loop
            row.append(value)
        grid.append(row)

def create_grid2(rows, cols, value):
    grid = [[value for i in range(rows)] for j in range(cols)]
    return grid
# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
print(create_grid2(3,4,0))