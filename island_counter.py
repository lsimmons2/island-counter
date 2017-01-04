
import numpy as np
import pandas as pd



class IslandCounter:



    def __init__(self, matrix):
        self.islands = []
        self.matrix = matrix
        self.find_islands()



    def get_matrix(self):
        return pd.DataFrame(np.array(self.matrix))



    def is_touching(self, a, b):
        if (a[0] == b[0] and abs(a[1]-b[1]) == 1) or (a[1] == b[1] and abs(a[0]-b[0]) == 1):
            return True
        return False



    def find_islands(self):

        # gets all the land_blocks, (any matrix element with value 1)
        # not sure if this should be it's own method, say find_land_blocks()
        # ============
        land_blocks = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    land_blocks.append((i,j))
        # ============

        islands = []

        while land_blocks:

            new_island = [land_blocks[0]]
            check_new_island = True

            while check_new_island:
                island_appended = False
                used_land_blocks = []
                for i in range(len(new_island)):
                    for j in range(1,len(land_blocks)):
                        if self.is_touching(new_island[i], land_blocks[j]):
                            new_island.append(land_blocks[j])
                            island_appended = True
                            used_land_blocks.append(j)
                    if used_land_blocks:
                        for island_appended in reversed(used_land_blocks):
                            land_blocks.pop(island_appended)
                        used_land_blocks = []
                if island_appended:
                    check_new_island = True
                else:
                    check_new_island = False
                    islands.append(new_island)


            if land_blocks:
                land_blocks.pop(0)


        self.islands = islands



    def get_islands(self):
        return self.islands



    def count_islands(self):
        return len(self.islands)




random_matrix = []
for i in range(0,5):
    row = []
    for j in range(0,5):
        row.append(np.random.randint(2))
    random_matrix.append(row)

random_island_counter = IslandCounter(random_matrix)
print 'random_matrix:\n', random_island_counter.get_matrix(), '\n'
print 'islands:\n', np.array(random_island_counter.get_islands()), '\n'
print '# of islands:\n', random_island_counter.count_islands(), '\n'


# row1 = [1,0,1,1,0]
# row2 = [0,0,1,1,0]
# row3 = [0,1,1,1,0]
# row4 = [1,0,1,0,1]
# row5 = [1,0,0,1,0]
# set_matrix = [row1, row2, row3, row4, row5]

row6 = [0,1,1,0,0,0,1]
row7 = [0,1,0,0,1,1,0]
row8 = [0,1,1,0,0,1,0]
row9 = [0,0,0,0,0,0,0]
row10 = [0,1,1,1,1,1,0]
set_matrix = [row6, row7, row8, row9, row10]

set_island_counter = IslandCounter(set_matrix)
print 'set_matrix:\n', set_island_counter.get_matrix(), '\n'
print 'islands:\n', np.array(set_island_counter.get_islands()), '\n'
print '# of islands:\n', set_island_counter.count_islands(), '\n'
