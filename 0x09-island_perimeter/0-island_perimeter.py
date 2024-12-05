#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns the perimeter of
the island described in grid:

    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to
    the water surrounding the island).
"""


def island_perimeter(grid):
    """
    A function def island_perimeter(grid): that returns the perimeter of
    the island described in grid    """
    # Initialize the perimeter counter
    perimeter = 0

    # Loop through each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if the current cell is land
            if grid[row][col] == 1:
                # Add 4 to the perimeter for the 4 sides of the land cell
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    # Return the total perimeter
    return perimeter
