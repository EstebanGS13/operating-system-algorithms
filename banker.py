import numpy as np

if __name__ == "__main__":
    resources = [6, 3, 4, 2]    # The total resources

    # The resources currently used by each process
    allocated = np.array([[3, 0, 1, 1],
                          [0, 1, 0, 0],
                          [1, 1, 1, 0],
                          [1, 1, 0, 1],
                          [0, 0, 0, 0]])

    # The resources each process needs
    need = np.array([[3, 0, 1, 1],
                     [0, 1, 0, 0],
                     [1, 1, 1, 0],
                     [1, 1, 0, 1],
                     [0, 0, 0, 0]])

    executed = [0] * allocated.shape[0]

    while not all(executed):
        available = resources - np.sum(allocated, axis=0)

        print(available)
        executed=[1,1,1,1,1]