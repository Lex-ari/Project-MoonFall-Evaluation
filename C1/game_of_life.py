import numpy as np
import time


class Game:
    def __init__(self, size=(8,8), seed=None, max_gen=100):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)
        
        # Initialize the board with a random series of 1s and 0s
        self._board = np.random.randint(0,2,size)
        self._gen = 0
        self._max_gen = max_gen
        self._list_of_alive_cells = []
        for row in range(self._board.shape[0]):
            for col in range(self._board.shape[1]):
                if self._board[row][col]: self._list_of_alive_cells.append((row, col))

    def update(self):
        board = np.copy(self._board)
        list_of_alive_cells = self._list_of_alive_cells.copy()
        ''' Insert your code for updating the board based on the rules below '''
        # refer to this index for cell orientation:
        # TL, T, TR
        # ML, ▇, MR
        # BL, B, BR
        neighbor_board_count = np.zeros(board.shape)
        neighbor_board_dictionary = {}  #stores plots in which a neighbor exists
        num_rows = board.shape[0]
        num_cols = board.shape[1]
        for (r, c) in list_of_alive_cells:
            hugging_top = r == 0 # if cell is hugging top border --> Disallow T additions
            hugging_bottom = r == num_rows - 1 #if cell is hugging bottom border --> Disallow B additions.
            if board[r][c]: # If cell exists in this plot, add 1 to its surrounding plots
                if c > 0:   # if not hugging left border, allow L additions
                    self.add_dictionary_plot(r, c - 1, neighbor_board_dictionary) #L
                    if not hugging_top: self.add_dictionary_plot(r - 1, c - 1, neighbor_board_dictionary)   #TL
                    if not hugging_bottom: self.add_dictionary_plot(r + 1, c - 1, neighbor_board_dictionary)    #BL
                if c < num_cols - 1: # if not hugging right border, allow R additions
                    self.add_dictionary_plot(r, c + 1, neighbor_board_dictionary) #R
                    if not hugging_top: self.add_dictionary_plot(r - 1, c + 1, neighbor_board_dictionary)   #TR
                    if not hugging_bottom: self.add_dictionary_plot(r + 1, c + 1, neighbor_board_dictionary)    #BR
                if not hugging_top: 
                    self.add_dictionary_plot(r - 1, c, neighbor_board_dictionary)   #T
                if not hugging_bottom: 
                    self.add_dictionary_plot(r + 1, c, neighbor_board_dictionary)   #B
        
        for (row, cow), neighbors in neighbor_board_dictionary.items():
            # importing Game of Life rules here:
            # Cell > 3 neighbors = dies
            # Cell 2-3 neighbors = lives 
            # Cell < 2 neighbors = dies
            # Dead cell with = 3 neighbors = lives
            if board[row][cow]: #If living cell exists on plot r,c
                if neighbors > 3 or neighbors < 2: 
                    board[row][cow] -= 1   #if alive cell, check for over/under population to determine death
                    list_of_alive_cells.remove((row, cow))
            elif neighbors == 3: 
                board[row][cow] += 1  #else (dead cell), check for neighbor population for life
                list_of_alive_cells.append((row, cow))
        self._board = board
        self._list_of_alive_cells = list_of_alive_cells


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

    def add_dictionary_plot(self, row, col, dict):
        if (row, col) in dict:
            dict[(row, col)] += 1
        else:
            dict.update({(row, col): 1})


if __name__ == "__main__":
    # If this file is run directly from the command line, run the game
    g = Game()
    g.time_run()
    #g.play()  # Uncomment this to see the generational progression