
from random import randint
import numpy as np
import pandas as pd


class IslandCounter:



    def __init__(self, input_matrix):
        self.input_matrix = input_matrix
        self.init_visited_matrix()
        self.row_count = len(input_matrix)
        self.col_count = len(input_matrix[0])
        self.count_islands()



    def init_visited_matrix(self):
        visited_matrix = []
        for i in range(len(self.input_matrix)):
            row = []
            for j in range(len(self.input_matrix[0])):
                row.append(False)
            visited_matrix.append(row)
        self.visited_matrix = visited_matrix



    def count_islands(self):
        self.count = 0
        for i in range(len(self.input_matrix)):
            for j in range(len(self.input_matrix[i])):
                if self.input_matrix[i][j] == 1 and not self.visited_matrix[i][j]:
                    self.count += 1
                    self.find_neighbors((i,j))



    def find_neighbors(self, (i,j)):
        self.visited_matrix[i][j] = True
        if i-1 > -1 and self.input_matrix[i-1][j] == 1 and not self.visited_matrix[i-1][j]:
            self.find_neighbors((i-1,j))
        if j-1 > -1 and self.input_matrix[i][j-1] == 1 and not self.visited_matrix[i][j-1]:
            self.find_neighbors((i,j-1))
        if j+1 < self.col_count and self.input_matrix[i][j+1] == 1 and not self.visited_matrix[i][j+1]:
            self.find_neighbors((i,j+1))
        if i+1 < self.row_count and self.input_matrix[i+1][j] == 1 and not self.visited_matrix[i+1][j]:
            self.find_neighbors((i+1,j))



    def get_matrix(self):
        return self.input_matrix



    def get_island_count(self):
        return self.count






random_matrix = []
for i in range(0,7):
    row = []
    for j in range(0,7):
        row.append(randint(0,1))
    random_matrix.append(row)

random_island_counter = IslandCounter(random_matrix)
print 'random_matrix:\n', pd.DataFrame(np.array(random_island_counter.get_matrix())), '\n'
print '# of islands:\n', random_island_counter.get_island_count(), '\n'



row1 = [0,1,1,0,0,0,1]
row2 = [0,1,0,0,1,1,0]
row3 = [0,1,1,0,0,1,0]
row4 = [0,0,0,0,0,0,0]
row5 = [0,1,1,1,1,1,0]
set_input_matrix = [row1, row2, row3, row4, row5]

set_island_counter = IslandCounter(set_input_matrix)

print 'set_matrix:\n', pd.DataFrame(np.array(set_island_counter.get_matrix())), '\n'
print '# of islands:\n', set_island_counter.get_island_count(), '\n'
