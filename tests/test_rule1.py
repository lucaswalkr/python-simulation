import numpy as np

# With rule 1, the fire (2) cells in the previous grid should become empty (0), 1's and 0's in previous grid should stay the same in the new grid

def test_rule1():
    previous_grid = np.array([[2, 1, 2], [2, 0, 2], [2, 1, 2]])
    expected_grid = np.array([[0, 1, 0], [0, 0, 0], [0, 1, 0]])

    new_grid = np.copy(previous_grid)
        
    for x in range(previous_grid.shape[0]):
        for y in range(previous_grid.shape[1]):

            # Getting the cell
            cell = previous_grid[x, y]

            # RULE 1: A burning cell in the previous time step turns into an empty cell
            if cell == 2:
                new_grid[x, y] = 0
    
            # If the rule doesn't match the cell remains un-changed from previous time step
            else:
                new_grid[x, y] = previous_grid[x, y]
                
    # Test to see if expected array is equal to output array, ran using 'pytest' in terminal
    np.testing.assert_array_equal(expected_grid, new_grid)