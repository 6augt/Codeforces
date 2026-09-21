n, m = map(int, input().split())
# N is the number of rows.
# M is the number of columns.

count = 0  # Create our counter
grid = []  # Create our grid

# For every row in N...
for row in range(n):
    grid.append(input())  # Add the map row to our grid

# For every row, excluding the first and last one...
for row in range(1, n - 1):

    # For every column, excluding the first and last one...
    for column in range(1, m - 1):

        # If the current cell is open...
        if grid[row][column] == '.':

            # If the cells above, below, and to the sides are all open...
            if grid[row + 1][column] == '.' and grid[row - 1][column] == '.' and grid[row][column + 1] == '.' and grid[row][column - 1] == '.':
                count += 1  # Add 1 to our counter

print(count)  # Print our counter
