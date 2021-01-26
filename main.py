import numpy as np
from transition_matrix import return_transition
from value_iteration import return_state_utility
from a_star import Enviroment_a_star

def main():



    Matrix = np.zeros((12, 12, 4))
    counter = 0
    for row in range(0, 3):
        for col in range(0, 4):
            line = return_transition(row, col, action="up", tot_row=3, tot_col=4)
            Matrix[counter, :, 0] = line.flatten()
            line = return_transition(row, col, action="left", tot_row=3, tot_col=4)
            Matrix[counter, :, 1] = line.flatten()
            line = return_transition(row, col, action="down", tot_row=3, tot_col=4)
            Matrix[counter, :, 2] = line.flatten()
            line = return_transition(row, col, action="right", tot_row=3, tot_col=4)
            Matrix[counter, :, 3] = line.flatten()

            counter += 1

    # Change as you want
    total_states = 12
    gamma = 0.2 # Discount factor
    iteration = 0  # Iteration counter
    epsilon = 0.001  # Stopping criteria small value


    # Reward vector
    r = np.array([-0.04, -0.04, -0.04, +1.0, -0.04, 0.0, -0.04, -1.0, -0.04, -0.04, -0.04, -0.04])

    # Utility vectors
    u = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    u1 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    while True:
        delta = 0
        u = u1.copy()
        iteration += 1
        for s in range(total_states):
            reward = r[s]
            v = np.zeros((1, total_states))
            v[0, s] = 1.0
            u1[s] = return_state_utility(v, Matrix, u, reward, gamma)
            delta = max(delta, np.abs(u1[s] - u[s]))

        print("---------------- ITERATIONS ----------------")
        print(u[0:4])
        print(u[4:8])
        print(u[8:12])
        # Stopping criteria
        if delta < epsilon * (1 - gamma) / gamma:
            print("---------------- FINAL RESULT ----------------")
            print("Iterations: " + str(iteration))
            print("Delta: " + str(delta))
            print("Gamma: " + str(gamma))
            print("Epsilon: " + str(epsilon))
            print("----------------------------------------------")
            print(u[0:4])
            print(u[4:8])
            print(u[8:12])
            print("===================================================")
            break


    enviroment = Enviroment_a_star(u)
    print(enviroment.compute_a_star())

if __name__ == "__main__":
    main()