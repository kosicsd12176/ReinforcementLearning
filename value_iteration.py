import numpy as np

def return_state_utility(v, T, u, reward, gamma):
    """Return the utility of a single state.
    This is an implementation of the Bellman equation.
    """
    action_array = np.zeros(4)
    for action in range(0, 4):
        action_array[action] = np.sum(np.multiply(u, np.dot(v, T[:,:,action])))
    return reward + gamma * np.max(action_array)



