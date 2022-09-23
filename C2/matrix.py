import numpy as np

class MatrixOps:
    def __init__(self, seed=None):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)

        self._matrix = np.random.randint(0,10, size=(10,10))
        self._kernel = np.random.randint(-2,2, size=(3,3))
    
    def largest_index(self, matrix):
        ''' Make this function return a tuple of the (row, col) 
            index of the largest value in the matrix '''
        num_rows = matrix.shape[0]
        num_cols = matrix.shape[1]
        max_int = 0
        max_index = [0, 0]
        for r in range(num_rows):
            for c in range(num_cols):
                if matrix[r][c] > max_int:
                    max_int = matrix[r][c]
                    max_index[0] = r
                    max_index[1] = c
        return tuple(max_index)

    def convolve(self, kernel, matrix):
        ''' Make this function return the result of a 2D convolution '''

        return matrix

    def run(self):
        print("Largest index is at ", self.largest_index(self._matrix))
        
        print("Result of convolution:")
        print(self.convolve(self._kernel, self._matrix))


if __name__ == "__main__":
    # If this file is run directly from the command line, run a test of the program
    m = MatrixOps()


    print("Running with matrix ")
    print(m._matrix)
    print("and kernel ")
    print(m._kernel)

    m.run() 