import numpy as np

# Rule 4 relies on the probability of an empty cell (0) filling with a tree (1).

# setting the probability as 0.5, to test that grid fills up with ~50% trees (1s)
p = 0.5

def test_rule4():
    previous_grid = np.zeros((100, 100))
    new_grid = np.copy(previous_grid)
    
    for x in range(previous_grid.shape[0]):
        for y in range(previous_grid.shape[1]):
            
            # RULE 4: An empty space fills with a tree with probability p
            if np.random.random() < p:
                new_grid[x, y] = 1
    
    # as there are only 0s and 1s in this test, the mean calculation == the proportion of ones present, should be roughly equal to p if code works
    proportion_of_ones = np.mean(new_grid)
    assert np.isclose(proportion_of_ones, p, atol=0.05)  # atol (tolerance) allows for some variance, +/- 5%