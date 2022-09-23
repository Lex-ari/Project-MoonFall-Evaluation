from xml.etree.ElementTree import tostring
import numpy as np
import time


class Game:
    def __init__(self, size=(8,8), seed=None, max_gen=10):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)
        
        # Initialize the board with a random series of 1s and 0s
        self._board = np.random.randint(0,2,size)
        self._gen = 0
        self._max_gen = max_gen

    
    def update(self):
        board = np.copy(self._board)
        
        ''' Insert your code for updating the board based on the rules below '''
        # refer to this index for cell orientation:
        # TL, T, TR
        # ML, ▇, MR
        # BL, B, BR
        neighbor_board_count = np.zeros(board.shape)
        num_rows = board.shape[0]
        num_cols = board.shape[1]
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c]:
                    hugging_top = r == 0 # if cell is hugging top border --> Disallow T additions
                    hugging_bottom = r == num_rows - 1 #if cell is hugging bottom border --> Disallow B additions.
                    if c > 0:   # if not hugging left border, allow L additions
                        neighbor_board_count[r][c - 1] += 1   #ML
                        if not hugging_top: neighbor_board_count[r - 1][c - 1] += 1   #TL
                        if not hugging_bottom: neighbor_board_count[r + 1][c - 1] += 1    #BL
                    if c < num_cols - 1: # if not hugging right border, allow R additions
                        neighbor_board_count[r][c + 1] += 1   #MR
                        if not hugging_top: neighbor_board_count[r - 1][c + 1] += 1   #TR
                        if not hugging_bottom: neighbor_board_count[r + 1][c + 1] += 1    #BR
                    if not hugging_top: neighbor_board_count[r - 1][c]  += 1   #T
                    if not hugging_bottom: neighbor_board_count[r + 1][c] += 1   #B
        
        for r in range(num_rows):
            for c in range(num_cols):
                # importing Game of Life rules here:
                # Cell > 3 neighbors = dies
                # Cell 2-3 neighbors = lives 
                # Cell < 2 neighbors = dies
                # Dead cell with >3 neighbors = lives
                if board[r][c]:
                    if neighbor_board_count[r][c] > 3 or neighbor_board_count[r][c] < 2: board[r][c] -= 1   #if alive cell, check for over/under population to determine death
                elif neighbor_board_count[r][c] == 3: board[r][c] += 1  #else (dead cell), check for neighbor population for life
        self._board = board


    def play(self, delay=.1):
        while self._gen < self._max_gen:
            # Start the generation by drawing the current board
            self.draw()
            
            # Next we update each of the cells according to the rules 
            self.update()

            # Increment the generation and sleep to make the visualization easier
            self._gen += 1
            time.sleep(delay)

    def time_run(self, gens=1000):
        start = time.time()
        for _ in range(gens):
            self.update()
        print(f'Average update time: {(time.time()-start)/gens*1000} ms')

    def draw(self):
        for row in self._board:   
            # Print a full block for each alive cell and an empty one for dead cells bounded by |
            print('|'.join(['▇' if c else ' ' for c in row]))

        print(f'Generation: {self._gen}')


if __name__ == "__main__":
    # If this file is run directly from the command line, run the game
    g = Game()
    #g.time_run()
    g.play()  # Uncomment this to see the generational progression