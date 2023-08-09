import numpy as np

# with rule 2 a tree (1) will set on fire (2) if at least 1 neighbour is burning.

def test_rule2():
    previous_grid = np.array([[0, 2, 0], [0, 1, 0], [0, 0, 0]])
    expected_grid = np.array([[0, 2, 0], [0, 2, 0], [0, 0, 0]])

    new_grid = np.copy(previous_grid)
        
    for x in range(previous_grid.shape[0]):
        for y in range(previous_grid.shape[1]):

            # Getting the cell and the four immediate neighbours
            cell = previous_grid[x, y]
            # Position of each neigbour cell relative to current cell, checks if cell is at                   boundary
            above = previous_grid[x-1, y] if x > 0 else 0
            below = previous_grid[x+1, y] if x < previous_grid.shape[0]-1 else 0
            left = previous_grid[x, y-1] if y > 0 else 0
            right = previous_grid[x, y+1] if y < previous_grid.shape[1]-1 else 0

            # Creating a list for 4 surrounding cells
            neighbours = [above, below, left, right]

            # RULE 2: A tree will start burning if at least one neighbour is burning
            if cell == 1:
                if 2 in neighbours:
                    new_grid[x, y] = 2
            
            # If the doesn't match, the cell remains un-changed from previous time step
            else:
                new_grid[x, y] = previous_grid[x, y]
    
    # Test to see if expected array is equal to output array, ran using 'pytest' in terminal
    np.testing.assert_array_equal(expected_grid, new_grid)