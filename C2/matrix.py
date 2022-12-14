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
        # refer to this index for index orientation:
        # TL, T, TR
        # ML, ▇, MR
        # BL, B, BR
        neighbor_board_count = np.zeros(matrix.shape)
        num_rows = matrix.shape[0]
        num_cols = matrix.shape[1]
        for r in range(num_rows):                
            hugging_top = r == 0 # if index is hugging top border --> Disallow T additions
            hugging_bottom = r == num_rows - 1 #if index is hugging bottom border --> Disallow B additions.
            for c in range(num_cols):   
                # for this implementation, each index is multiplying and adding itself to its neighbors according to an opposites kernel 
                # this means adding to a TR neighbor means multiplying the current index by the BL value of the kernel.
                index_value = matrix[r][c]
                neighbor_board_count[r][c] += index_value * kernel[1][1] # weight applied to self
                if c > 0:   # if not hugging left border, allow L additions
                    neighbor_board_count[r][c - 1] += index_value * kernel[1][2]  #ML   (MR Kernel)
                    if not hugging_top: neighbor_board_count[r - 1][c - 1] += index_value * kernel[2][2]  #TL   (BR Kernel)
                    if not hugging_bottom: neighbor_board_count[r + 1][c - 1] += index_value * kernel[0][2]   #BL   (TR Kernel)
                if c < num_cols - 1: # if not hugging right border, allow R additions
                    neighbor_board_count[r][c + 1] += index_value * kernel[1][0]  #MR   (ML Kernel)
                    if not hugging_top: neighbor_board_count[r - 1][c + 1] += index_value * kernel[2][0]  #TR   (BL Kernel)
                    if not hugging_bottom: neighbor_board_count[r + 1][c + 1] += index_value * kernel[0][0]   #BR   (TL Kernel)
                if not hugging_top: neighbor_board_count[r - 1][c] += index_value * kernel[2][1]  #T    (B Kernel)
                if not hugging_bottom: neighbor_board_count[r + 1][c] += index_value * kernel[0][1]  #B (T Kernel)
        for r in range(num_rows):
            for c in range(num_cols):
                matrix[r][c] = neighbor_board_count[r][c]
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