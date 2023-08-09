# A forest-fire model following the principles of a cellular automaton model
# Student ID: 1930864
# University of Bristol

import numpy as np

# Set the seed for pseudo-randomness
np.random.seed(7)

def initialise_state(num_steps, initial_state):
    """
    Initialise the grid with the initial state of the system, create an empty array to store the state at each time step
    
    Args:
        num_steps (int): number of time steps in the simulation
        initial state (list, np.ndarray): the 2-dimensional initial state of the model
    
    Returns:
        grid (list, np.ndarray): a 2-dimensional array to store the state at each time step, beginning with the initial state
    """
    grid = np.zeros((num_steps, *initial_state.shape), dtype=np.int32) # takes array size from the shape of the initial state, type integer
    grid[0] = initial_state # setting initial state
    return grid

def update_state(previous_grid):
    """
    Update the state of the grid based on previous state, according the four forest-fire rules in order
    
    Args:
        previous_grid (np.ndarray): The previous 2-dimensional state of the grid
    
    Returns:
        new_grid (np.ndarray): The new, updated, 2-dimensional state of the grid
    """
    new_grid = np.copy(previous_grid)
    
    #Getting every cell by looking at each row (x) and column (y) coordinate
    for x in range(previous_grid.shape[0]):
        for y in range(previous_grid.shape[1]):
            
            # Getting the cell and the four immediate neighbours
            cell = previous_grid[x, y]
            # Position of each neigbour cell relative to current cell, checks if cell is at             boundary
            above = previous_grid[x-1, y] if x > 0 else 0
            below = previous_grid[x+1, y] if x < previous_grid.shape[0]-1 else 0
            left = previous_grid[x, y-1] if y > 0 else 0
            right = previous_grid[x, y+1] if y < previous_grid.shape[1]-1 else 0
            
            # Creating a list for 4 surrounding cells
            neighbours = [above, below, left, right]
            
            # 4 rules of the system, checked in order
            # Rule 1: A burning cell in the previous time step turns into an empty cell
            if cell == 2:
                new_grid[x, y] = 0
               
            # Rule 2: A tree will start burning if at least one neighbour is burning
            elif cell == 1:
                if 2 in neighbours:
                    new_grid[x, y] = 2
            
                # Rule 3: A tree turns into fire with probability F
                elif np.random.random() < f:
                    new_grid[x, y] = 2

            # Rule 4: An empty space fills with a tree with probability P
            elif np.random.random() < p:
                new_grid[x, y] = 1
                
            # Cell remains unchanged if no rules match 
            else:
                new_grid[x, y] = previous_grid[x, y]
                    
    return new_grid

def run_simulation(num_steps, initial_state):
    """
    Runs the simulation for a given number of steps, using the initialise_state function to set the state and the update_state function to iterate the state according to the system rules in update_state
    
    Args:
        num_steps (int): number of time steps that will be run by the simulation
        initial_state (list, np.ndarray): the 2-dimensional initial state of the grid
    
    Returns: 
        state (list, np.ndarray): the overall state for the system
    """
    state = initialise_state(num_steps, initial_state)
    
    for t in range(1, num_steps):
        state[t] = update_state(state[t-1]) # looping over state with update_state function based on state in previous time step
        
    return state

# FOR STEADY STATE SET FRACTION OF TREES = 0.5, f = 0.02 and p = 0.1

# The probability of a tree catching fire due to lightning strike (1 --> 2)
f = 0.02
# The probability of an empty space becoming a tree due to tree growth (0 --> 1)
p = 0.1

# The fraction of the forest covered by trees
fraction_of_trees = 0.5
# The initial state of the forest, a 100x100 grid filled with empty (0) and tree (1) cells
initial_state = np.random.binomial(1, fraction_of_trees, size=(100, 100))

# The number of time steps (t) that the simulation will run for
num_steps = 200

# Save simulation to object "grid"
grid = run_simulation(num_steps, initial_state)

# Saving the numpy grid to file "forest_simulation.npz"
np.savez_compressed("forest_simulation", state=grid)
