import numpy as np


def return_transition(row, col, action, tot_row, tot_col):

    if(row > tot_row-1 or col > tot_col-1):
        print("ERROR: the index is out of range...")
        return None

    world = np.zeros((tot_row+2, tot_col+2))


    #If the state is on the grey-obstacle it returns all zeros
    if(row == 1 and col == 1): return world[1:4, 1:5]
    #If the process is on the final reward state it returns zeros
    if(row == 0 and col == 3): return world[1:4, 1:5]
    #If the process is on the final punishment state then returns zeros
    if(row == 1 and col == 3): return world[1:4, 1:5]

    if(action=="up"):
            col += 1
            row += 1
            world[row-1, col] = 0.8
            world[row, col+1] = 0.1
            world[row, col-1] = 0.1
    elif(action=="down"):
            col += 1
            row += 1
            world[row+1, col] = 0.8
            world[row, col+1] = 0.1
            world[row, col-1] = 0.1
    elif(action=="left"):
            col += 1
            row += 1
            world[row-1, col] = 0.1
            world[row+1, col] = 0.1
            world[row, col-1] = 0.8
    elif(action=="right"):
            col += 1
            row += 1
            world[row-1, col] = 0.1
            world[row+1, col] = 0.1
            world[row, col+1] = 0.8

    #Reset the obstacle
    if(world[2, 2] != 0): world[row, col] += world[2, 2]
    world[2, 2] = 0.0

    #Control bouncing
    for row in range(0, 5):
            if(world[row, 0] != 0): world[row, 1] += world[row, 0]
            if(world[row, 5] != 0): world[row, 4] += world[row, 5]
    for col in range(0, 6):
            if(world[0, col] != 0): world[1, col] += world[0, col]
            if(world[4, col] != 0): world[3, col] += world[4, col]


    #print(world[1:4, 1:5])
    #print(world.shape)
    return world[1:4, 1:5]






